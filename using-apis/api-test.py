'''
api-test.py
Kate Sweeney, 2018-10-01

Returns data from Star Wars API swapi.co
Prints either a list of names of films, people, planets, species,
starships, or vehicles or a dictionary of specific information
for one of those with a certain ID.

Ex: python3 api-test.py people 1
returns dictionary of information about Luke Skywalker (ID #1)

python3 api-test.py people
returns a list of all people in the Star Wars API
'''

import sys
import json
import urllib.request

def parse_command_line():
    if len(sys.argv) == 3:
        type_and_id = {"type": sys.argv[1],"id": sys.argv[2]}
        return type_and_id
    elif len(sys.argv) == 2:
        type_and_id = {"type": sys.argv[1],"id": None}
        return type_and_id
    else:
        handle_error()

def get_page_data(type_and_id,*,successive_page = False, given_url = None):
    try:
        #some data sets are multi-page and the url comes from the previous page
        if successive_page is False:
            base_url = 'https://swapi.co/api/{0}/{1}'
            if type_and_id["id"] is None:
                url = base_url.format(type_and_id["type"],"")
            else:
                url = base_url.format(type_and_id["type"],type_and_id["id"])
        else:
            url = given_url
        request = urllib.request.Request(url)
        request.add_header('User-Agent',"temp")
        data_from_server = urllib.request.urlopen(request).read()
        string_from_server = data_from_server.decode('utf-8')
        dict_of_data = json.loads(string_from_server)
        return dict_of_data
    except:
        handle_error()

def get_list_of_names(type_and_id,dict_of_type,list_of_names):
    if dict_of_type["next"] is None:
        for i in dict_of_type["results"]:
            #key for name for "films" is "title" instead of "names"
            try:
                list_of_names.append(i["name"])
            except:
                list_of_names.append(i["title"])
        return list_of_names
    #some data is on multiple pages; reads the next page and recurses
    #to check all pages
    if not (dict_of_type["next"] is None):
        for i in dict_of_type["results"]:
            try:
                list_of_names.append(i["name"])
            except:
                list_of_names.append(i["title"])
        dict_page_next = get_page_data(type_and_id,successive_page=True,given_url=dict_of_type["next"])
        return get_list_of_names(type_and_id,dict_page_next,list_of_names)

def print_list_of_names(list_of_names):
    for i in list_of_names:
        print(i)

def print_item_info(dict_of_item):
    print(json.dumps(dict_of_item, indent = 4))

def get_item_with_id(type_and_id):
    dict_of_item = get_page_data(type_and_id)
    return dict_of_item


def handle_error():
    print("Usage: python3 api-test.py category [id-number]", file=sys.stderr)
    exit()

def main():
    type_and_id = parse_command_line()

    if type_and_id["id"] is None:
        dict_of_type = get_page_data(type_and_id)
        list_of_names = get_list_of_names(type_and_id,dict_of_type,[])
        print_list_of_names(list_of_names)
    else:
        dict_of_item_info = get_item_with_id(type_and_id)
        print_item_info(dict_of_item_info)

if __name__== "__main__":
    main()