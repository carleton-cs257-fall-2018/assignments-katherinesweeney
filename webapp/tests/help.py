import csv


look ="pl_pnum INT,pl_orbper INT,pl_orbsmax INT,pl_orbeccen INT,pl_massj INT,pl_radj INT,pl_dens INT,pl_nnotes INT"


reader = csv.reader(open("test_planets.csv", newline=''))

planets = []

found = ""

for row in reader:
    if ((row[0])[0]) != "#":
        if found == "":
            found = row
        else:
            planet = {}
            for k in range(0,len(found)):
                if (found[k]+ " ") in look and row[k] != "":
                    planet.update({found[k]:float(row[k])})
                else:
                    planet.update({found[k]: row[k]})

            print(planet)
            print()
            planets.append(planet)

#print(planets)


