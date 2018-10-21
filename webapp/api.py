#!/usr/bin/env python3
'''
    example_flask_app.py
    Jeff Ondich, 22 April 2016

    A slightly more complicated Flask sample app than the
    "hello world" app found at http://flask.pocoo.org/.
'''
import sys
import flask
import json

app = flask.Flask(__name__)

import psycopg2
import psycopg2.extras

from config import password
from config import database
from config import user


names_planet = ["pl_id", "pl_host_star_id", "pl_name", "pl_discmethod_id", "pl_orbper",
         "pl_orbsmax", "pl_orbeccen", "pl_massj", "pl_bmassprov", "pl_radj",
         "pl_dens", "pl_ttvflag", "pl_kepflag", "pl_k2flag", "pl_nnotes",
         "row_update", "pl_facility_id"]

names_star = ["st_id", "st_planet_1_name_id", "st_planet_2_name_id", "st_planet_3_name_id",
              "st_planet_4_name_id", "st_planet_5_name_id", "st_planet_6_name_id",
              "st_planet_7_name_id", "st_planet_8_name_id","st_name", "s_pnum", "st_dist",
              "st_teff", "st_mass","st_rad", "row_update"]


try:
    connection = psycopg2.connect(database=database, user=user, password=password)
except Exception as e:
    print(e)
    exit()


@app.route('/planet/<pl_name>')
def get_planet(pl_name):
    '''
    Gets a planet with the given name
    '''
    planets = []
    cursor = connection.cursor()
    query = '''SELECT *
               FROM planets
               WHERE pl_name = %s'''
    try:
        cursor.execute(query, (pl_name,))
    except Exception as e:
        print(e)
        exit()

    for row in cursor:
        planet = {}
        for i in range(0, len(row)):
            planet.update({names_planet[i]: str(row[i])})

        planets.append(planet)

    return json.dumps(planets)

@app.route('/star/<st_name>')
def get_star(st_name):
    '''
    Gets a star with the given name
    '''
    stars = []
    cursor = connection.cursor()
    query = '''SELECT *
               FROM stars
               WHERE st_name = %s'''
    try:
        cursor.execute(query, (st_name,))
    except Exception as e:
        print(e)
        exit()

    for row in cursor:
        star = {}
        for i in range(0, len(row)):
            star.update({names_star[i]: str(row[i])})

        stars.append(star)

    return json.dumps(stars)

@app.route('/planets/datafields')
def get_planets_datafields():
    return json.dumps(names_planet)

@app.route('/stars/datafields')
def get_stars_datafields():
    return json.dumps(names_star)

@app.route('/planets')
def get_planets():

    pl_name = flask.request.args.get('pl_name', default="", type=str)
    pl_hostname = flask.request.args.get('pl_hostname', default="", type=str)
    pl_discmethod = flask.request.args.get('pl_discmethod', default="", type=str)
    pl_pnum = flask.request.args.get('pl_pnum', default=-1, type=int)
    pl_pnummax = flask.request.args.get('pl_pnummax', default=9, type=int)
    pl_pnummin = flask.request.args.get('pl_pnummin', default=0, type=int)
    pl_orbper = flask.request.args.get('pl_orbper', default=-1, type=float)
    pl_orbpermax = flask.request.args.get('pl_orbpermax', default=8000000, type=float)
    pl_orbpermin = flask.request.args.get('pl_orbpermin', default=0, type=float)
    pl_orbsmax = flask.request.args.get('pl_orbsmax', default=-1, type=float)
    pl_orbsmaxmax = flask.request.args.get('pl_orbsmaxmax', default=2600, type=float)
    pl_orbsmaxmin = flask.request.args.get('pl_orbsmaxmin', default=0, type=float)
    pl_eccen = flask.request.args.get('pl_eccen', default=-1, type=float)
    pl_eccenmax = flask.request.args.get('pl_eccenmax', default=1, type=float)
    pl_eccenmin = flask.request.args.get('pl_eccenmin', default=0, type=float)
    pl_massj = flask.request.args.get('pl_massj', default=-1, type=float)
    pl_massjmax = flask.request.args.get('pl_massjmax', default=60, type=float)
    pl_massjmin = flask.request.args.get('pl_massjmin', default=0, type=float)
    pl_radj = flask.request.args.get('pl_radj', default=-1, type=float)
    pl_radjmax = flask.request.args.get('pl_radjmax', default=7, type=float)
    pl_radjmin = flask.request.args.get('pl_radjmin', default=0, type=float)
    pl_dens = flask.request.args.get('pl_dens', default=-1, type=float)
    pl_densmax = flask.request.args.get('pl_densmax', default=80, type=float)
    pl_densmin = flask.request.args.get('pl_densmin', default=0, type=float)
    pl_ttvflag = flask.request.args.get('pl_ttvflag', default="", type=str)
    pl_kepflag = flask.request.args.get('pl_kepflag', default="", type=str)
    pl_k2flag = flask.request.args.get('pl_k2flag', default="", type=str)
    pl_nnotes = flask.request.args.get('pl_nnotes', default=-1, type=int)
    pl_nnotesmax = flask.request.args.get('pl_nnotesmax', default=5, type=int)
    pl_nnotesmin = flask.request.args.get('pl_nnotesmin', default=0, type=int)
    pl_facility = flask.request.args.get('pl_facility', default="", type=str)


    planets = []
    cursor = connection.cursor()
    query = '''SELECT planets.*
               FROM planets, stars, discovery_methods, discovery_facility
               WHERE planets.pl_name LIKE %s
               AND planets.pl_host_star_id = stars.st_id 
               AND planets.pl_discmethod_id = discovery_methods.discmeth_id
               AND planets.pl_facility_id = discovery_facility.disc_facil_id
               AND stars.st_name LIKE %s
               AND discovery_methods.name LIKE %s
               AND (%s = -1 OR (planets.pl_host_star_id = stars.st_id AND stars.st_pnum = %s ))
               AND (stars.st_pnum <= %s OR (stars.st_pnum IS NULL AND %s = 9))
               AND (stars.st_pnum >= %s OR (stars.st_pnum IS NULL AND %s = 0))
               AND (planets.pl_orbper = %s OR %s = -1)
               AND (planets.pl_orbper <= %s OR (planets.pl_orbper IS NULL AND %s = 8000000))
               AND (planets.pl_orbper >= %s OR (planets.pl_orbper IS NULL AND %s = 0))
               AND (planets.pl_orbsmax = %s OR %s = -1)
               AND (planets.pl_orbsmax <= %s OR (planets.pl_orbsmax IS NULL AND %s = 2600))
               AND (planets.pl_orbsmax >= %s OR (planets.pl_orbsmax IS NULL AND %s = 0))
               AND (planets.pl_orbeccen = %s OR %s = -1)
               AND (planets.pl_orbeccen <= %s OR (planets.pl_orbeccen IS NULL AND %s = 1))
               AND (planets.pl_orbeccen >= %s OR (planets.pl_orbeccen IS NULL AND %s = 0))
               AND (planets.pl_massj = %s OR %s = -1)
               AND (planets.pl_massj <= %s OR (planets.pl_massj IS NULL AND %s = 60))
               AND (planets.pl_massj >= %s OR (planets.pl_massj IS NULL AND %s = 0))
               AND (%s = -1 OR planets.pl_radj = %s)
               AND (planets.pl_radj <= %s OR (planets.pl_radj IS NULL AND %s = 7))
               AND (planets.pl_radj >= %s OR (planets.pl_radj IS NULL AND %s = 0))
               AND (%s = -1 OR planets.pl_dens = %s)
               AND (planets.pl_dens <= %s OR (planets.pl_dens IS NULL AND %s = 80))
               AND (planets.pl_dens >= %s OR (planets.pl_dens IS NULL AND %s = 0))
               AND (%s = '' or planets.pl_ttvflag = %s)
               AND (%s = '' or planets.pl_kepflag = %s)
               AND (%s = '' or planets.pl_k2flag = %s)
               AND (%s = -1 OR planets.pl_nnotes = %s)
               AND (planets.pl_nnotes <= %s OR (planets.pl_nnotes IS NULL AND %s = 5))
               AND (planets.pl_nnotes >= %s OR (planets.pl_nnotes IS NULL AND %s = 0))
               AND (discovery_facility.name LIKE %s)
               '''

    try:
        cursor.execute(query, ( ("%" + pl_name + "%"),("%" + pl_hostname + "%"),
                                ("%" + pl_discmethod + "%"),pl_pnum,pl_pnum,pl_pnummax,pl_pnummax,
                                pl_pnummin,pl_pnummin,pl_orbper,pl_orbper,pl_orbpermax,pl_orbpermax,
                                pl_orbpermin,pl_orbpermin,pl_orbsmax,pl_orbsmax,pl_orbsmaxmax,pl_orbsmaxmax,
                                pl_orbsmaxmin,pl_orbsmaxmin,pl_eccen,pl_eccen,pl_eccenmax,pl_eccenmax,pl_eccenmin,
                                pl_eccenmin,pl_massj,pl_massj,pl_massjmax,pl_massjmax,pl_massjmin,pl_massjmin,
                                pl_radj,pl_radj,pl_radjmax,pl_radjmax,pl_radjmin,pl_radjmin,pl_dens,pl_dens,
                                pl_densmax,pl_densmax,pl_densmin,pl_densmin,pl_ttvflag,pl_ttvflag,pl_kepflag,
                                pl_kepflag,pl_k2flag,pl_k2flag,pl_nnotes,pl_nnotes,pl_nnotesmax,pl_nnotesmax,
                                pl_nnotesmin,pl_nnotesmin,("%" + pl_facility + "%")))

    except Exception as e:
        print(e)
        exit()

    for row in cursor:
        planet = {}
        for i in range(0, len(row)):
            planet.update({names_planet[i]: str(row[i])})

        planets.append(planet)

    return json.dumps(planets)

@app.route('/stars')
def get_stars():
    st_name = flask.request.args.get('st_name', default="", type=str)
    st_pnum = flask.request.args.get('st_pnum', default=-1, type=int)
    st_pnummax = flask.request.args.get('st_pnummax', default=9, type=int)
    st_pnummin = flask.request.args.get('st_pnummin', default=0, type=int)
    st_planet_1_name = flask.request.args.get('st_planet_1_name', default="", type=str)
    st_planet_2_name = flask.request.args.get('st_planet_2_name', default="", type=str)
    st_planet_3_name = flask.request.args.get('st_planet_3_name', default="", type=str)
    st_planet_4_name = flask.request.args.get('st_planet_4_name', default="", type=str)
    st_planet_5_name = flask.request.args.get('st_planet_5_name', default="", type=str)
    st_planet_6_name = flask.request.args.get('st_planet_6_name', default="", type=str)
    st_planet_7_name = flask.request.args.get('st_planet_7_name', default="", type=str)
    st_planet_8_name = flask.request.args.get('st_planet_8_name', default="", type=str)
    st_dist = flask.request.args.get('st_dist', default=-1, type=float)
    st_distmax = flask.request.args.get('st_distmax', default=9000, type=float)
    st_distmin = flask.request.args.get('st_distmin', default=0, type=float)
    st_teff = flask.request.args.get('st_teff', default=-1, type=float)
    st_teffmax= flask.request.args.get('st_teffmax', default=60000, type=float)
    st_teffmin = flask.request.args.get('st_teffmin', default=0, type=float)
    st_mass = flask.request.args.get('st_mass', default=-1, type=float)
    st_massmax = flask.request.args.get('st_massmax', default=25, type=float)
    st_massmin = flask.request.args.get('st_massmin', default=0, type=float)
    st_rad = flask.request.args.get('st_rad', default=-1, type=float)
    st_radmax = flask.request.args.get('st_radmax', default=75, type=float)
    st_radmin= flask.request.args.get('st_radmin', default=0, type=float)

    stars = []
    cursor = connection.cursor()
    query = '''SELECT stars.*
               FROM stars, planets
               WHERE stars.st_name LIKE %s
               AND (%s = -1 OR stars.st_pnum = %s)
               AND (stars.st_pnum <= %s OR (stars.st_pnum IS NULL AND %s = 9))
               AND (stars.st_pnum >= %s OR (stars.st_pnum IS NULL AND %s = 0))
               AND planets.pl_host_star_id = stars.st_id 
               AND (%s = '' OR (stars.st_planet_1_name_id = planets.pl_id AND planets.pl_name LIKE %s))
               AND (%s = '' OR (stars.st_planet_2_name_id = planets.pl_id AND planets.pl_name LIKE %s))
               AND (%s = '' OR (stars.st_planet_3_name_id = planets.pl_id AND planets.pl_name LIKE %s))
               AND (%s = '' OR (stars.st_planet_4_name_id = planets.pl_id AND planets.pl_name LIKE %s))
               AND (%s = '' OR (stars.st_planet_5_name_id = planets.pl_id AND planets.pl_name LIKE %s))
               AND (%s = '' OR (stars.st_planet_6_name_id = planets.pl_id AND planets.pl_name LIKE %s))
               AND (%s = '' OR (stars.st_planet_7_name_id = planets.pl_id AND planets.pl_name LIKE %s))
               AND (%s = '' OR (stars.st_planet_8_name_id = planets.pl_id AND planets.pl_name LIKE %s))
               '''

    try:
        cursor.execute(query, ( ("%" + st_name + "%"),st_pnum,st_pnum,st_pnummax,st_pnummax,st_pnummin,st_pnummin,
                                st_planet_1_name,("%" + st_planet_1_name + "%"),st_planet_2_name,("%" + st_planet_2_name + "%"),
                                st_planet_3_name,("%" + st_planet_3_name + "%"),st_planet_4_name,("%" + st_planet_4_name + "%"),
                                st_planet_5_name,("%" + st_planet_5_name + "%"),st_planet_6_name,("%" + st_planet_6_name + "%"),
                                st_planet_7_name,("%" + st_planet_7_name + "%"),st_planet_8_name,("%" + st_planet_8_name + "%")))
    except Exception as e:
        print(e)
        exit()

    for row in cursor:
        star = {}

        for i in range(0, len(row)):
            star.update({names_star[i]: str(row[i])})
        stars.append(star)

    return json.dumps(stars)



if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]))
        print('  Example: {0} perlman.mathcs.carleton.edu 5101'.format(sys.argv[0]))
        exit()
    
    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port, debug=True)
