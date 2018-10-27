# import csv
#
#
# # look ="pl_pnum INT,pl_orbper INT,pl_orbsmax INT,pl_orbeccen INT,pl_massj INT,pl_radj INT,pl_dens INT,pl_nnotes INT"
#
#
# reader = csv.reader(open("new_planet.csv", newline=''))
#
# planets = []
#
# found = ""
#
# for row in reader:
#     if ((row[0])[0]) != "#":
#         if found == "":
#             found = row
#         else:
#             planet = {}
#             for k in range(0,len(found)):
#                 if found[k].find("err") == -1 and found[k].find("lim") == -1:
#                     planet.update({found[k]: row[k]})
#
#             # print(planet)
#             # print()
#             planets.append(planet)
# print(planets)
#
#
# import csv
#
#
# keys = list(planets[0].keys())
# print(keys)
#
# with open('final_planets.csv', 'w') as csvfile:
#     fieldnames = keys
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     for k in planets:
#         writer.writerow(k)
# import csv
#
#
# reader = csv.reader(open("final_stars.csv", newline=''))
#
# id = []
# stars = []
#
# stars_we_have = set()
#
# for row in reader:
#     if id == []:
#         id = row
#     else:
#         star = {}
#         for i in range(0,len(id)):
#             star.update({id[i] : row[i]})
#             star.update({"st_planet_1_name_id" : None})
#             star.update({"st_planet_2_name_id": None})
#             star.update({"st_planet_3_name_id": None})
#             star.update({"st_planet_4_name_id": None})
#             star.update({"st_planet_5_name_id": None})
#             star.update({"st_planet_6_name_id": None})
#             star.update({"st_planet_7_name_id": None})
#             star.update({"st_planet_8_name_id": None})
#
#         if not row[9] in stars_we_have:
#             stars_we_have.add(row[9])
#             stars.append(star)
#
# reader = csv.reader(open("final_planets.csv", newline=''))
#
# id = []
# planets = []
# for row in reader:
#     if id == []:
#         id = row
#     else:
#         planet = {}
#         for i in range(0,len(id)):
#             planet.update({id[i] : row[i]})
#         planets.append(planet)
#         for star in stars:
#             if star["pl_hostname"] == planet["pl_hostname"]:
#                 if star["st_planet_1_name_id"] == None:
#                     star["st_planet_1_name_id"] = planet["loc_rowid"]
#                 elif star["st_planet_2_name_id"] == None:
#                     star["st_planet_2_name_id"] = planet["loc_rowid"]
#                 elif star["st_planet_3_name_id"] == None:
#                     star["st_planet_3_name_id"] = planet["loc_rowid"]
#                 elif star["st_planet_4_name_id"] == None:
#                     star["st_planet_4_name_id"] = planet["loc_rowid"]
#                 elif star["st_planet_5_name_id"] == None:
#                     star["st_planet_5_name_id"] = planet["loc_rowid"]
#                 elif star["st_planet_6_name_id"] == None:
#                     star["st_planet_6_name_id"] = planet["loc_rowid"]
#                 elif star["st_planet_7_name_id"] == None:
#                     star["st_planet_7_name_id"] = planet["loc_rowid"]
#                 elif star["st_planet_8_name_id"] == None:
#                     star["st_planet_8_name_id"] = planet["loc_rowid"]
#
# print(stars)
# keys = list(stars[0].keys())
# with open('final_stars.csv', 'w') as csvfile:
#     fieldnames = keys
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     for k in stars:
#         writer.writerow(k)

import csv
reader = csv.reader(open("final_stars.csv", newline=''))
id = []
stars = []
for row in reader:
    if id == []:
        id = row
    else:
        star = {}
        for i in range(0,len(id)):
            star.update({id[i] : row[i]})
        stars.append(star)


reader = csv.reader(open("discfacility.csv", newline=''))
id = []
fac = []
for row in reader:
    if id == []:
        id = row
    else:
        star = {}
        for i in range(0,len(id)):
            star.update({id[i] : row[i]})
        fac.append(star)


reader = csv.reader(open("discmethod.csv", newline=''))
id = []
disc = []
for row in reader:
    if id == []:
        id = row
    else:
        star = {}
        for i in range(0,len(id)):
            star.update({id[i] : row[i]})
        disc.append(star)


reader = csv.reader(open("final_planets.csv", newline=''))
id = []
planets = []
for row in reader:
    if id == []:
        id = row
    else:
        planet = {}
        for i in range(0,len(id)):
            if id[i] == "pl_hostname":
                for k in stars:
                    if k["pl_hostname"] == row[i]:
                        planet.update({id[i]: k["loc_rowid"]})
            elif id[i] == "pl_facility":
                for k in fac:
                    if k["pl_facility"] == row[i]:
                        planet.update({id[i] : k["loc_rowid"]})
            elif id[i] == "pl_discmethod":
                for k in disc:
                    if k["pl_discmethod"] == row[i]:
                        planet.update({id[i] : k["loc_rowid"]})
            else:
                planet.update({id[i] : row[i]})
        planets.append(planet)
print(planets)


keys = list(planets[0].keys())
with open('final_planets.csv', 'w') as csvfile:
    fieldnames = keys
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for k in planets:
        writer.writerow(k)