# -*- coding: utf-8 -*-

import os
import sqlite3
import db
import simplejson, urllib.request
import math
from math import sin, cos, sqrt, atan2, radians

db=db.DB('database.sqlite')

stateId = input("Insert State Id: ")

cityCount = db.get_number_cities(stateId)
print("Number of cities in state:", cityCount)

cities = db.get_cities(stateId)

initialIndex = int(input("Starting index for cities: "))
secondaryIndex = int(input("Starting index for second city: "))

# 101 231
# &key=AIzaSyCdUNvXpeJOcbVkpftzw95h2Ip6P_eQP_c
# approximate radius of earth in km
R = 6373.0

if (secondaryIndex == initialIndex):
    db.insert_distance_row(cities[initialIndex]['id'], cities[initialIndex]['id'], 0)
    secondaryIndex += 1

for j in range (secondaryIndex, cityCount):
    print("city1Id (index):", cities[initialIndex]['id'], '(',initialIndex,')', "city2Id (index):", cities[j]['id'], '(',j,')')
    # orig = "%f,%f" % (cities[initialIndex]['lat'], cities[initialIndex]['lon'])
    # dest = "%f,%f" % (cities[j]['lat'], cities[j]['lon'])
    # url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false&key=AIzaSyCdUNvXpeJOcbVkpftzw95h2Ip6P_eQP_c".format(str(orig), str(dest))
    # result = simplejson.load(urllib.request.urlopen(url))
    # print(result)
    # driving_distance = result['rows'][0]['elements'][0]['distance']['value'] / 1000.0
    lat1 = radians(cities[initialIndex]['lat'])
    lon1 = radians(cities[initialIndex]['lon'])
    lat2 = radians(cities[j]['lat'])
    lon2 = radians(cities[j]['lon'])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    print("Result:", distance)
    db.insert_distance_row(cities[initialIndex]['id'], cities[j]['id'], distance)
        
for i in range(initialIndex+1, cityCount):
    db.insert_distance_row(cities[i]['id'], cities[i]['id'], 0)
    for j in range (i+1, cityCount):
        print("city1Id (index):", cities[i]['id'], '(',i,')', "city2Id (index):", cities[j]['id'], '(',j,')')
        # orig = "%f,%f" % (cities[i]['lat'], cities[i]['lon'])
        # dest = "%f,%f" % (cities[j]['lat'], cities[j]['lon'])
        # url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false&key=AIzaSyCdUNvXpeJOcbVkpftzw95h2Ip6P_eQP_c".format(str(orig), str(dest))
        # result = simplejson.load(urllib.request.urlopen(url))
        # print(result)
        # driving_distance = result['rows'][0]['elements'][0]['distance']['value'] / 1000.0
        lat1 = radians(cities[i]['lat'])
        lon1 = radians(cities[i]['lon'])
        lat2 = radians(cities[j]['lat'])
        lon2 = radians(cities[j]['lon'])

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        print("Result:", distance)
        db.insert_distance_row(cities[i]['id'], cities[j]['id'], distance)

db.conn.commit()