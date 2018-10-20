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


    planets = []
    cursor = connection.cursor()
    query = '''SELECT planets.*
               FROM planets, stars, discovery_methods
               WHERE planets.pl_name LIKE %s
               AND planets.pl_host_star_id = stars.st_id 
               AND stars.st_name LIKE %s
               AND planets.pl_discmethod_id = discovery_methods.discmeth_id
               AND discovery_methods.name LIKE %s'''
    print("start")
    try:
        cursor.execute(query, ( ("%" + pl_name + "%"),("%" + pl_hostname + "%"),
                                ("%" + pl_discmethod + "%") ))
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
