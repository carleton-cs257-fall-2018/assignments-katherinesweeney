#!/usr/bin/env python3
#Authors Owen Barnett and Katherine Sweeney
import sys
import flask
import json
import psycopg2

import config

app = flask.Flask(__name__, static_folder='static', template_folder='templates')

names_planet = ["Planet Id", "Host Star ID", "Planet Name", "Planet Discovery Method ID", "Planet Orbital Period (Days)",
                "Planet Orbital Period Semi-Major Axis (AU)", "Planet Orbital Eccentricity", "Planet Jupiter Mass",
                "Planet Mass Provenance", "Planet Jupiter Radius", "Planet Density (g/cm^3)", "Planet TTV Flag",
                "Planet Kepler Flag", "Planet Kepler 2 Flag", "Number of Notes on Planet", "Last Updated",
                "Planet Discovery Facility ID", "Planet Discovery Method", "Planet Discovery Facility", "Host Star Name"]

names_star = ["Star Id", "First Planet in System", "Second Planet in System", "Third Planet in System",
              "Fourth Planet in System", "Fifth Planet in System", "Sixth Planet in System",
              "Seventh Planet in System", "Eighth Planet in System","Star Name", "Number of Planets In System",
              "Distance From Earth (pc)", "Tempurature (K)", "Mass (Solar Masses)","Radius (Solar Radii)", "Last Updated"]


def get_connection():

    connection = None
    try:
        connection = psycopg2.connect(database=config.database,
                                      user=config.user,
                                      password=config.password)
    except Exception as e:
        print(e, file=sys.stderr)
    return connection

def get_select_query_results(connection, query, parameters=None):
    '''
    Executes the specified query with the specified tuple of
    parameters. Returns a cursor for the query results.

    Raises an exception if the query fails for any reason.
    '''
    cursor = connection.cursor()
    if parameters is not None:
        cursor.execute(query, parameters)
    else:
        cursor.execute(query)
    return cursor


@app.route('/planet/<pl_id>')
def get_planet(pl_id):
    '''
    Gets a planet with the given name
    '''
    planets = []
    connection = get_connection()
    cursor = connection.cursor()
    query = '''SELECT *
               FROM planets
               WHERE pl_id = %s'''
    try:
        cursor.execute(query, (pl_id,))
    except Exception as e:
        print(e)
        exit()

    for row in cursor:
        planet = {}
        for i in range(0, len(row)):
            planet.update({names_planet[i]: str(row[i])})

        planets.append(planet)

    return json.dumps(planets)

@app.route('/star/<st_id>')
def get_star(st_id):
    '''
    Gets a star with the given name
    '''
    stars = []
    connection = get_connection()
    cursor = connection.cursor()
    query = '''SELECT *
               FROM stars
               WHERE st_id = %s'''
    try:
        cursor.execute(query, (st_id,))
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

@app.route('/star_id/<st_id>')
def get_star_id(st_id):
    '''
    Gets a star with the given name
    '''
    stars = []
    connection = get_connection()
    cursor = connection.cursor()
    query = '''SELECT *
               FROM stars
               WHERE st_id = %s'''
    try:
        cursor.execute(query, (st_id,))
    except Exception as e:
        print(e)
        exit()
    for row in cursor:
        star = {}
        for i in range(0, len(row)):
            star.update({names_star[i]: str(row[i])})
        stars.append(star)
    return json.dumps(stars)

@app.route('/planet_id/<pl_id>')
def get_planet_id(pl_id):
    '''
    Gets a planet with the given name
    '''
    planets = []
    connection = get_connection()
    cursor = connection.cursor()
    query = '''SELECT *
               FROM planets
               WHERE pl_id = %s'''
    try:
        cursor.execute(query, (pl_id,))
    except Exception as e:
        print(e)
        exit()
    for row in cursor:
        planet = {}
        for i in range(0, len(row)):
            planet.update({names_planet[i]: str(row[i])})
        planets.append(planet)
    return json.dumps(planets)

@app.route('/facility_id/<facility_id>')
def get_facility_id(facility_id):
    '''
    Gets a star with the given name
    '''
    facilities = []
    connection = get_connection()
    cursor = connection.cursor()
    query = '''SELECT *
               FROM discovery_facility
               WHERE disc_facil_id = %s'''
    try:
        cursor.execute(query, (facility_id,))
    except Exception as e:
        print(e)
        exit()
    for row in cursor:
        facility = {"disc_facil_id":row[0], "name":row[1]}
        facilities.append(facility)
    return json.dumps(facilities)

@app.route('/disc_method_id/<disc_method_id>')
def get_discmethod_id(disc_method_id):
    '''
    Gets a star with the given name
    '''
    methods = []
    connection = get_connection()
    cursor = connection.cursor()
    query = '''SELECT *
               FROM discovery_methods
               WHERE discmeth_id = %s'''
    try:
        cursor.execute(query, (disc_method_id,))
    except Exception as e:
        print(e)
        exit()
    for row in cursor:
        method = {"discmeth_id":row[0], "name":row[1]}
        methods.append(method)
    return json.dumps(methods)

@app.route('/planets')
def get_planets():
    '''
    Gets a list of dictionaries of the planets that satisfy the given constraints
    from the URL and returns a json string
    '''
    pl_id = flask.request.args.get('pl_id', default=-1, type=int)
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
    connection = get_connection()
    cursor = connection.cursor()
    query = '''SELECT planets.*, discovery_methods.name, discovery_facility.name, stars.st_name
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
               AND (%s = -1 OR planets.pl_id = %s)
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
                                pl_nnotesmin,pl_nnotesmin,("%" + pl_facility + "%"),pl_id,pl_id))

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
    '''
    Gets a list of dictionaries of the planets that satisfy the given constraints
    from the URL and returns a json string
    '''
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
    connection = get_connection()
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
               AND (stars.st_dist = %s OR %s = -1)
               AND (stars.st_dist <= %s OR (stars.st_dist IS NULL AND %s = 900))
               AND (stars.st_dist >= %s OR (stars.st_dist IS NULL AND %s = 0))
               AND (stars.st_teff = %s OR %s = -1)
               AND (stars.st_teff <= %s OR (stars.st_teff IS NULL AND %s = 60000))
               AND (stars.st_teff >= %s OR (stars.st_teff IS NULL AND %s = 0))
               AND (stars.st_mass = %s OR %s = -1)
               AND (stars.st_mass <= %s OR (stars.st_mass IS NULL AND %s = 25))
               AND (stars.st_mass >= %s OR (stars.st_mass IS NULL AND %s = 0))
               AND (stars.st_rad = %s OR %s = -1)
               AND (stars.st_rad <= %s OR (stars.st_rad IS NULL AND %s = 75))
               AND (stars.st_rad >= %s OR (stars.st_rad IS NULL AND %s = 0))
               '''

    try:
        cursor.execute(query, ( ("%" + st_name + "%"),st_pnum,st_pnum,st_pnummax,st_pnummax,st_pnummin,st_pnummin,
                                st_planet_1_name,("%" + st_planet_1_name + "%"),st_planet_2_name,("%" + st_planet_2_name + "%"),
                                st_planet_3_name,("%" + st_planet_3_name + "%"),st_planet_4_name,("%" + st_planet_4_name + "%"),
                                st_planet_5_name,("%" + st_planet_5_name + "%"),st_planet_6_name,("%" + st_planet_6_name + "%"),
                                st_planet_7_name,("%" + st_planet_7_name + "%"),st_planet_8_name,("%" + st_planet_8_name + "%"),
                                st_dist,st_dist,st_distmax,st_distmax,st_distmin,st_distmin,st_teff,st_teff,st_teffmax,st_teffmax,
                                st_teffmin,st_teffmin,st_mass,st_mass,st_massmax,st_massmax,st_massmin,st_massmin,st_rad,st_rad,
                                st_radmax,st_radmax,st_radmin,st_radmin))
    except Exception as e:
        print(e)
        exit()

    for row in cursor:
        star = {}

        for i in range(0, len(row)):
            star.update({names_star[i]: str(row[i])})
        if not star in stars:
            stars.append(star)

    return json.dumps(stars)

@app.after_request
def set_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=int(port), debug=True)
