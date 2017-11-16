# -*- coding: utf-8 -*-

import os
import sqlite3
import db
import simplejson, urllib.request
import math
from math import sin, cos, sqrt, atan2, radians

db=db.DB('database.sqlite')

for stateId in range(1, 13):
	cities = db.get_cities(stateId)

	cityCount = db.get_number_cities(stateId)
	# approximate radius of earth in km
	R = 6373.0

	for i in range(0, cityCount):
		db.insert_distance_row(cities[i]['id'], cities[i]['id'], 0)
		for j in range (i+1, cityCount):
			print("city1Id (index):", cities[i]['id'], '(',i,')', "city2Id (index):", cities[j]['id'], '(',j,')')
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
	input('Press enter to continue')
