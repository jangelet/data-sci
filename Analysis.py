import folium
import pandas as pd
import math
import json
#active license data up until January 1, 2017

def licensePlotter():

    inputFile1 = pd.read_csv('active_license.csv')

    inputFile2 = pd.read_csv('complaint_data.csv')

    map = folium.Map(location=[40.853279, -73.876496], tiles='Stamen Toner', zoom_start=12)

    #loops through rows of inputFile, pulling coordinates
    for index, row in inputFile1.iterrows():
        if not (math.isnan(row["Latitude"]) and math.isnan(row["Longitude"])):
            lati  = row["Latitude"]
            longi = row["Longitude"]
            label = row["License Type Name"]
            folium.RegularPolygonMarker([lati, longi], fill_color ='#006080', popup=label, number_of_sides=4, radius=10).add_to(map)

    for index, row in inputFile2.iterrows():
        if not (math.isnan(row["Latitude"]) and math.isnan(row["Longitude"])):
            lati = row["Latitude"]
            longi = row["Longitude"]
            label = row["PD_DESC"]
            folium.RegularPolygonMarker([lati, longi], fill_color ='#ff4d4d', popup=label, number_of_sides=3, radius=10).add_to(map)

    #creates html file of map
    map.save('licenseMap.html')

licensePlotter()