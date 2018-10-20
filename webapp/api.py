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
    planet = ""
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
        planet = row
	return (planet)





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
