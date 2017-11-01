from scipy.spatial import Voronoi
import csv
import folium
from geojson import FeatureCollection, Feature, Polygon

coords = []
names = []

mapVor = folium.Map(location=[40.75, -73.9],tiles="Cartodb Positron",zoom_start=13)

with open('CUNY.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        lat = float(row[7])
        lon = float(row[8])
        name = row[1]
        coords.append([lat,lon])
        folium.Marker([lat, lon],popup = name).add_to(mapVor)

vor = Voronoi(coords)

vorJSON = open('CUNYVor.json', 'w')
point_voronoi_list = []
feature_list = []
for region in range(len(vor.regions)-1):
    vertex_list = []
    for x in vor.regions[region]:
        if x == -1:
            break
        else:
            vertex = vor.vertices[x]
            vertex = (vertex[1], vertex[0])
        vertex_list.append(vertex)
    polygon = Polygon([vertex_list])
    feature = Feature(geometry=polygon, properties={})
    feature_list.append(feature)

feature_collection = FeatureCollection(feature_list)
print (feature_collection, file=vorJSON)
vorJSON.close()

mapVor.choropleth(geo_path='CUNYVor.json',fill_color="BuPu", fill_opacity=0.01,line_opacity=0.25)

mapVor.save(outfile='CUNYVor.html')



