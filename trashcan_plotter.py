import folium
import pandas as pd
import math
import csv
from itertools import islice
import operator

xcoords = []
ycoords = []

dist = []
trashdict = {}

def main():

    with open('Litter_Basket_Inventory.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in islice(reader, 0, 5000):
            xcoords.append(float(row[1]))
            ycoords.append(float(row[2]))

        #calculates Euclidean distance, populates new array

        map = folium.Map(location=[xcoords[3459], ycoords[3459]])

        inner_value = 0
        for k in range(0, 4999):
            folium.Marker([xcoords[k], ycoords[kzzzzzzzzzzx]], popup="Trashcan", icon=folium.Icon(color="green")).add_to(map)

            inner_value += ((xcoords[k] - xcoords[k+1]) + (ycoords[k] - ycoords[k+1])) ** 2
            dist.append(math.sqrt(inner_value))
            trashdict[k] = math.sqrt(inner_value)
            inner_value = 0

        sorted_trashdict = sorted(trashdict.items(), key=operator.itemgetter(1))

    print(sorted_trashdict)

    print(xcoords[3459], ycoords[3459])

    print(math.sqrt((xcoords[3459] - xcoords[3460]) + (ycoords[3459] - ycoords[3460])) ** 2)

    folium.Marker([xcoords[3459], ycoords[3459]], popup="Trashcan", icon=folium.Icon(color="green")).add_to(map)

    map.save('trashcanMap.html')

main()


