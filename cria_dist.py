# -*- coding: utf-8 -*-

import os
import sqlite3
import db
import simplejson, urllib.request

db=db.DB('database.sqlite')

states = db.get_states()

stateId = input("Insert State Id: ")

cityCount = db.get_number_cities(stateId)
print("Number of cities in state:", cityCount)

cities = db.get_cities(stateId)

initialIndex = int(input("Starting index for cities: "))
secondaryIndex = int(input("Starting index for second city: "))

#40 235

if (secondaryIndex == initialIndex):
    db.insert_distance_row(cities[initialIndex]['id'], cities[initialIndex]['id'], 0)
    secondaryIndex += 1

for j in range (secondaryIndex, cityCount):
    print("city1Id (index):", cities[initialIndex]['id'], '(',initialIndex,')', "city2Id (index):", cities[j]['id'], '(',j,')')
    orig = "%f,%f" % (cities[initialIndex]['lat'], cities[initialIndex]['lon'])
    dest = "%f,%f" % (cities[j]['lat'], cities[j]['lon'])
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false&key=AIzaSyCdUNvXpeJOcbVkpftzw95h2Ip6P_eQP_c".format(str(orig), str(dest))
    result = simplejson.load(urllib.request.urlopen(url))
    print(result)
    driving_distance = result['rows'][0]['elements'][0]['distance']['value'] / 1000.0
    db.insert_distance_row(cities[initialIndex]['id'], cities[j]['id'], driving_distance)
        
for i in range(initialIndex+1, cityCount):
    db.insert_distance_row(cities[i]['id'], cities[i]['id'], 0)
    for j in range (i+1, cityCount):
        print("city1Id (index):", cities[i]['id'], '(',i,')', "city2Id (index):", cities[j]['id'], '(',j,')')
        orig = "%f,%f" % (cities[i]['lat'], cities[i]['lon'])
        dest = "%f,%f" % (cities[j]['lat'], cities[j]['lon'])
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false&key=AIzaSyCdUNvXpeJOcbVkpftzw95h2Ip6P_eQP_c".format(str(orig), str(dest))
        result = simplejson.load(urllib.request.urlopen(url))
        print(result)
        driving_distance = result['rows'][0]['elements'][0]['distance']['value'] / 1000.0
        db.insert_distance_row(cities[i]['id'], cities[j]['id'], driving_distance)

db.conn.commit()