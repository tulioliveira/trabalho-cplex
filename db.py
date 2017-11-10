# -*- coding: utf-8 -*-
import os
import sys
import sqlite3


class DB(object):
    def __init__(self, fileName):
        self.db_connect(fileName)

    def __del__(self):
        self.conn.close()

    def db_connect(self, fileName):
        if (os.path.isfile(fileName) == False):
           print("sqlite database file {:s} not found!".format(fileName))
           sys.exit(-1)
        self.conn = sqlite3.connect(fileName)

    def get_states(self):
        cur = self.conn.cursor()
        cur.execute("select id, uf from states")
        states = [[row[0], str(row[1])] for row in cur.fetchall()]
        return states

    def get_state_by_id(self, ufid):
        cur = self.conn.cursor()
        cur.execute("select * from states where id = '{_ufid}'".format(_ufid=ufid))
        row = cur.fetchone()
        state = {"id": row[0], "uf": row[1], "name": row[2], "nCities": row[3], "minPop": row[4], "maxPop": row[5]}
        return state

    def get_cities(self, ufid):
        cur = self.conn.cursor()
        cur.execute(
            "select * from cities where state_id = '{_ufid}'".format(_ufid=ufid))
        cities = [{"id": row[0], "name": row[3], "lat": row[4],
                   "lon": row[5], "pop": row[6]} for row in cur.fetchall()]
        return cities

    def get_number_cities(self, ufid):
        cur = self.conn.cursor()
        cur.execute(
            "select count(*) from cities where state_id = '{_ufid}'".format(_ufid=ufid))
        return cur.fetchone()[0]

    def get_number_ranged_cities(self, ufid, pop_a=0, pop_b=sys.maxsize):
        cur = self.conn.cursor()
        cur.execute("select count(*) from cities where state_id = '{_ufid}' and pop >= {_pop_a} and pop <= {_pop_b}".format(
            _ufid=ufid, _pop_a=pop_a, _pop_b=pop_b))
        return cur.fetchone()[0]

    def get_ranged_cities(self, ufid, pop_a=0, pop_b=sys.maxsize):
        cur = self.conn.cursor()
        cur.execute("select * from cities where state_id = '{_ufid}' and pop >= {_pop_a} and pop <= {_pop_b}".format(
            _ufid=ufid, _pop_a=pop_a, _pop_b=pop_b))
        cities = [{"id": row[0], "name": row[3], "lat": row[4],
                   "lon": row[5], "pop": row[6]} for row in cur.fetchall()]
        return cities

    def get_max_pop(self, ufid):
        cur = self.conn.cursor()
        cur.execute(
            "select max(pop) from cities where state_id = '{_ufid}'".format(_ufid=ufid))
        return cur.fetchone()[0]

    def get_min_pop(self, ufid):
        cur = self.conn.cursor()
        cur.execute(
            "select min(pop) from cities where state_id = '{_ufid}'".format(_ufid=ufid))
        return cur.fetchone()[0]

    def create_distance_table(self):
        cur = self.conn.cursor()
        
        sql = "CREATE TABLE IF NOT EXISTS 'dist' ( 'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 'city1_id' INTEGER NOT NULL, 'city2_id' INTEGER NOT NULL, 'distance' REAL NOT NULL, FOREIGN KEY('city1_id') REFERENCES 'cities'('id'), FOREIGN KEY('city2_id') REFERENCES 'cities'('id') )"
        cur.execute(sql)
        self.conn.commit()

    def insert_distance_row(self, city1Id, city2Id, distance):
        cur = self.conn.cursor()
        sql = "INSERT INTO dist (city1_id, city2_id, distance)" + \
            "VALUES ({_city1Id}, {_city2Id}, {_distance})".format(
                _city1Id=city1Id, _city2Id=city2Id, _distance=distance)
        cur.execute(sql)
        self.conn.commit()

    def get_cities_by_population_range(self, stateId, minPop=0, maxPop=sys.maxsize): 
        cur = self.conn.cursor()
        sql = "SELECT id, name, lat, lon, pop FROM cities WHERE state_id = {_stateId} AND pop > {_minPop} AND pop < {_maxPop}".format(
            _stateId=stateId, _minPop=minPop, _maxPop=maxPop)
        cur.execute(sql)
        cities = [{"index": idx+1, "cityId": row[0], "name": row[1], "lat": row[2],
                   "lon": row[3], "pop": row[4]} for idx, row in enumerate(cur.fetchall())]
        return cities

    def get_distance(self, cityId1, cityId2):
        cur = self.conn.cursor()
        sql = "SELECT distance FROM dist WHERE (city1_id = {_cityId1} AND city2_id = {_cityId2}) OR (city1_id = {_cityId2} AND city2_id = {_cityId1})".format(
            _cityId1=cityId1, _cityId2=cityId2)
        cur.execute(sql)
        print("{:d} -> {:d}".format(cityId1, cityId2))
        return cur.fetchone()[0]
