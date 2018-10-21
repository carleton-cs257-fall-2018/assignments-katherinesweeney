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
    pl_pnummax = flask.request.args.get('pl_pnummax', default=sys.maxsize, type=int)
    pl_pnummin = flask.request.args.get('pl_pnummin', default=-sys.maxsize, type=int)
    pl_orbper = flask.request.args.get('pl_orbper', default=-1, type=float)
    pl_orbpermax = flask.request.args.get('pl_orbpermax', default=sys.maxsize, type=float)
    pl_orbpermin = flask.request.args.get('pl_orbpermin', default=0, type=float)
    pl_orbsmax = flask.request.args.get('pl_orbsmax', default=-1, type=float)
    pl_orbsmaxmax = flask.request.args.get('pl_orbsmaxmax', default=sys.maxsize, type=float)
    pl_orbsmaxmin = flask.request.args.get('pl_orbsmaxmin', default=0, type=float)
    pl_eccen = flask.request.args.get('pl_eccen', default=-1, type=float)
    pl_eccenmax = flask.request.args.get('pl_eccenmax', default=sys.maxsize, type=float)
    pl_eccenmin = flask.request.args.get('pl_eccenmin', default=0, type=float)
    pl_massj = flask.request.args.get('pl_massj', default=-1, type=float)
    pl_massjmax = flask.request.args.get('pl_massjmax', default=sys.maxsize, type=float)
    pl_massjmin = flask.request.args.get('pl_massjmin', default=0, type=float)
    pl_massprov = flask.request.args.get('pl_massprov', default="", type=str)
    pl_radj = flask.request.args.get('pl_radj', default=-sys.maxsize, type=float)
    pl_radjmax = flask.request.args.get('pl_radjmax', default=sys.maxsize, type=float)
    pl_radjmin = flask.request.args.get('pl_radjmin', default=-sys.maxsize, type=float)
    pl_dens = flask.request.args.get('pl_dens', default=-sys.maxsize, type=float)
    pl_densmax = flask.request.args.get('pl_densmax', default=sys.maxsize, type=float)
    pl_densmin = flask.request.args.get('pl_densmin', default=-sys.maxsize, type=float)
    pl_ttvflag = flask.request.args.get('pl_ttvflag', default="", type=str)
    pl_kepflag = flask.request.args.get('pl_kepflag', default="", type=str)
    pl_k2flag = flask.request.args.get('pl_k2flag', default="", type=str)
    pl_nnotes = flask.request.args.get('pl_nnotes', default=-sys.maxsize, type=int)
    pl_nnotesmax = flask.request.args.get('pl_nnotesmax', default=sys.maxsize, type=int)
    pl_nnotesmin = flask.request.args.get('pl_nnotesmin', default=-sys.maxsize, type=int)
    pl_facility = flask.request.args.get('pl_facility', default="", type=str)
    row_update = flask.request.args.get('row_update', default="", type=str)


    planets = []
    cursor = connection.cursor()
    query = '''SELECT planets.*
               FROM planets, stars, discovery_methods
               WHERE planets.pl_name LIKE %s
               AND planets.pl_host_star_id = stars.st_id 
               AND planets.pl_discmethod_id = discovery_methods.discmeth_id
               AND stars.st_name LIKE %s
               AND discovery_methods.name LIKE %s
               AND (%s = -1 OR (planets.pl_host_star_id = stars.st_id AND stars.st_pnum = %s ))
               AND stars.st_pnum <= %s 
               AND stars.st_pnum >= %s
               AND (planets.pl_orbper = %s OR %s = -1)
               AND planets.pl_orbper <= %s
               AND planets.pl_orbper >= %s
               AND (planets.pl_orbsmax = %s OR %s = -1)
               AND planets.pl_orbsmax <= %s
               AND planets.pl_orbsmax >= %s
               AND (planets.pl_orbeccen = %s OR %s = -1)
               AND planets.pl_orbeccen <= %s
               AND planets.pl_orbeccen >= %s
               AND (planets.pl_massj = %s OR %s = -1)
               AND planets.pl_massj <= %s
               AND planets.pl_massj >= %s
               AND planets.pl_bmassprov = 'Mass'
               '''
    print("start")
    try:
        cursor.execute(query, ( ("%" + pl_name + "%"),("%" + pl_hostname + "%"),
                                ("%" + pl_discmethod + "%"),pl_pnum,pl_pnum,pl_pnummax,
                                pl_pnummin,pl_orbper,pl_orbper,pl_orbpermax,pl_orbpermin,
                                pl_orbsmax,pl_orbsmax,pl_orbsmaxmax,pl_orbsmaxmin,
                                pl_eccen,pl_eccen,pl_eccenmax,pl_eccenmin,pl_massj,
                                pl_massj,pl_massjmax,pl_massjmin ))
    except Exception as e:
        print(e)
        exit()
    print("done")
    for row in cursor:
        planet = {}
        for i in range(0, len(row)):
            planet.update({names_planet[i]: str(row[i])})

        planets.append(planet)

    return json.dumps(planets)

@app.route('/stars')
def get_stars():
    st_name = flask.request.args.get('st_name', default="", type=str)
    st_pnum = flask.request.args.get('st_pnum', default=-sys.maxsize, type=int)
    st_pnummax = flask.request.args.get('st_pnummax', default=sys.maxsize, type=int)
    st_pnummin = flask.request.args.get('st_pnummin', default=-sys.maxsize, type=int)
    st_planet_1_name = flask.request.args.get('st_planet_1_name', default="", type=str)
    st_planet_2_name = flask.request.args.get('st_planet_2_name', default="", type=str)
    st_planet_3_name = flask.request.args.get('st_planet_3_name', default="", type=str)
    st_planet_4_name = flask.request.args.get('st_planet_4_name', default="", type=str)
    st_planet_5_name = flask.request.args.get('st_planet_5_name', default="", type=str)
    st_planet_6_name = flask.request.args.get('st_planet_6_name', default="", type=str)
    st_planet_7_name = flask.request.args.get('st_planet_7_name', default="", type=str)
    st_planet_8_name = flask.request.args.get('st_planet_8_name', default="", type=str)
    st_dist = flask.request.args.get('st_dist', default=-sys.maxsize, type=float)
    st_distmax = flask.request.args.get('st_distmax', default=sys.maxsize, type=float)
    st_distmin = flask.request.args.get('st_distmin', default=-sys.maxsize, type=float)
    st_teff = flask.request.args.get('st_teff', default=-sys.maxsize, type=float)
    st_teffmax= flask.request.args.get('st_teffmax', default=sys.maxsize, type=float)
    st_teffmin = flask.request.args.get('st_teffmin', default=-sys.maxsize, type=float)
    st_mass = flask.request.args.get('st_mass', default=-sys.maxsize, type=float)
    st_massmax = flask.request.args.get('st_massmax', default=sys.maxsize, type=float)
    st_massmin = flask.request.args.get('st_massmin', default=-sys.maxsize, type=float)
    st_rad = flask.request.args.get('st_rad', default=-sys.maxsize, type=float)
    st_radmax = flask.request.args.get('st_radmax', default=sys.maxsize, type=float)
    st_radmin= flask.request.args.get('st_radmin', default=-sys.maxsize, type=float)
    row_update = flask.request.args.get('row_update', default="", type=str)

    pass


# @app.route('/')
# def hello():
#     return 'Hello, Citizen of CS257.'
#
# @app.route('/actor/<last_name>')
# def get_actor(last_name):
#     ''' Returns the first matching actor, or an empty dictionary if there's no match. '''
#     actor_dictionary = {}
#     lower_last_name = last_name.lower()
#     for actor in actors:
#         if actor['last_name'].lower().startswith(lower_last_name):
#             actor_dictionary = actor
#             break
#     return json.dumps(actor_dictionary)
#
# @app.route('/movies')
# def get_movies():
#     ''' Returns the list of movies that match GET parameters:
#           start_year, int: reject any movie released earlier than this year
#           end_year, int: reject any movie released later than this year
#           genre: reject any movie whose genre does not match this genre exactly
#         If a GET parameter is absent, then any movie is treated as though
#         it meets the corresponding constraint. (That is, accept a movie unless
#         it is explicitly rejected by a GET parameter.)
#     '''
#     movie_list = []
#     genre = flask.request.args.get('genre')
#     start_year = flask.request.args.get('start_year', default=0, type=int)
#     end_year = flask.request.args.get('end_year', default=10000, type=int)
#     for movie in movies:
#         if genre is not None and genre != movie['genre']:
#             continue
#         if movie['year'] < start_year:
#             continue
#         if movie['year'] > end_year:
#             continue
#         movie_list.append(movie)
#
#     return json.dumps(movie_list)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]))
        print('  Example: {0} perlman.mathcs.carleton.edu 5101'.format(sys.argv[0]))
        exit()
    
    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port, debug=True)
