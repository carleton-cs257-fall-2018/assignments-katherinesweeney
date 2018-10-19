import csv


# look ="pl_pnum INT,pl_orbper INT,pl_orbsmax INT,pl_orbeccen INT,pl_massj INT,pl_radj INT,pl_dens INT,pl_nnotes INT"


reader = csv.reader(open("new_planet.csv", newline=''))

planets = []

found = ""

for row in reader:
    if ((row[0])[0]) != "#":
        if found == "":
            found = row
        else:
            planet = {}
            for k in range(0,len(found)):
                planet.update({found[k]: row[k]})

            # print(planet)
            # print()
            planets.append(planet)

print(planets)


import csv


keys = list(planets[0].keys())
print(keys)

with open('final_planets.csv', 'w') as csvfile:
    fieldnames = keys
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for k in planets:
        writer.writerow(k)


