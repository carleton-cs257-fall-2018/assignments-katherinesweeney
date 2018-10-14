#Authors: Owen Barnett and Katherine Sweeney


import api
import unittest


#  The planet and star dictionaries are very long, so I will make global variables up here for each planet and star

planet1 = {'loc_rowid': '1', 'pl_hostname': '11 Com', 'pl_name': '11 Com b', 'pl_discmethod': 'Radial Velocity',
           'pl_pnum': 1.0, 'pl_orbper': 326.03, 'pl_orbpererr1': '0.32000000', 'pl_orbpererr2': '-0.32000000',
           'pl_orbperlim': '0', 'pl_orbsmax': 1.29, 'pl_orbsmaxerr1': '0.050000', 'pl_orbsmaxerr2': '-0.050000',
           'pl_orbsmaxlim': '0', 'pl_orbeccen': 0.231, 'pl_orbeccenerr1': '0.005000', 'pl_orbeccenerr2': '-0.005000',
           'pl_orbeccenlim': '0', 'pl_bmassj': '19.40000', 'pl_bmassjerr1': '1.50000', 'pl_bmassjerr2': '-1.50000',
           'pl_bmassjlim': '0', 'pl_bmassprov': 'Msini', 'pl_radj': '', 'pl_radjerr1': '', 'pl_radjerr2': '',
           'pl_radjlim': '', 'pl_dens': '', 'pl_denserr1': '', 'pl_denserr2': '', 'pl_denslim': '', 'pl_ttvflag': '0',
           'pl_kepflag': '0', 'pl_k2flag': '0', 'pl_nnotes': 0.0, 'st_dist': '93.37', 'st_disterr1': '1.92',
           'st_disterr2': '-1.92', 'st_distlim': '0', 'st_teff': '4742.00', 'st_tefferr1': '100.00', 'st_tefferr2': '-100.00',
           'st_tefflim': '0', 'st_mass': '2.70', 'st_masserr1': '0.30', 'st_masserr2': '-0.30', 'st_masslim': '0',
           'st_rad': '19.00', 'st_raderr1': '2.00', 'st_raderr2': '-2.00', 'st_radlim': '0', 'rowupdate': '2014-05-14',
           'pl_facility': 'Xinglong Station'}

planet2 = {'loc_rowid': '2', 'pl_hostname': '11 UMi', 'pl_name': '11 UMi b', 'pl_discmethod': 'Radial Velocity',
           'pl_pnum': 1.0, 'pl_orbper': 516.21997, 'pl_orbpererr1': '3.20000000', 'pl_orbpererr2': '-3.20000000',
           'pl_orbperlim': '0', 'pl_orbsmax': 1.53, 'pl_orbsmaxerr1': '0.070000', 'pl_orbsmaxerr2': '-0.070000',
           'pl_orbsmaxlim': '0', 'pl_orbeccen': 0.08, 'pl_orbeccenerr1': '0.030000', 'pl_orbeccenerr2': '-0.030000',
           'pl_orbeccenlim': '0', 'pl_bmassj': '14.74000', 'pl_bmassjerr1': '2.50000', 'pl_bmassjerr2': '-2.50000',
           'pl_bmassjlim': '0', 'pl_bmassprov': 'Msini', 'pl_radj': '', 'pl_radjerr1': '', 'pl_radjerr2': '',
           'pl_radjlim': '0', 'pl_dens': '', 'pl_denserr1': '', 'pl_denserr2': '', 'pl_denslim': '0', 'pl_ttvflag': '0',
           'pl_kepflag': '0', 'pl_k2flag': '0', 'pl_nnotes': 0.0, 'st_dist': '125.72', 'st_disterr1': '1.97',
           'st_disterr2': '-1.97', 'st_distlim': '0', 'st_teff': '4213.00', 'st_tefferr1': '46.00', 'st_tefferr2': '-46.00',
           'st_tefflim': '0', 'st_mass': '2.78', 'st_masserr1': '0.69', 'st_masserr2': '-0.69', 'st_masslim': '0',
           'st_rad': '29.79', 'st_raderr1': '2.84', 'st_raderr2': '-2.84', 'st_radlim': '0', 'rowupdate': '2018-09-06',
           'pl_facility': 'Thueringer Landessternwarte Tautenburg'}

planet3 = {'loc_rowid': '3', 'pl_hostname': '14 And', 'pl_name': '14 And b', 'pl_discmethod': 'Radial Velocity',
           'pl_pnum': 1.0, 'pl_orbper': 185.84, 'pl_orbpererr1': '0.23000000', 'pl_orbpererr2': '-0.23000000',
           'pl_orbperlim': '0', 'pl_orbsmax': 0.83, 'pl_orbsmaxerr1': '', 'pl_orbsmaxerr2': '', 'pl_orbsmaxlim': '0',
           'pl_orbeccen': 0.0, 'pl_orbeccenerr1': '', 'pl_orbeccenerr2': '', 'pl_orbeccenlim': '0', 'pl_bmassj': '4.80000',
           'pl_bmassjerr1': '', 'pl_bmassjerr2': '', 'pl_bmassjlim': '0', 'pl_bmassprov': 'Msini', 'pl_radj': '',
           'pl_radjerr1': '', 'pl_radjerr2': '', 'pl_radjlim': '', 'pl_dens': '', 'pl_denserr1': '', 'pl_denserr2': '',
           'pl_denslim': '', 'pl_ttvflag': '0', 'pl_kepflag': '0', 'pl_k2flag': '0', 'pl_nnotes': 0.0, 'st_dist': '75.59',
           'st_disterr1': '0.71', 'st_disterr2': '-0.71', 'st_distlim': '0', 'st_teff': '4813.00', 'st_tefferr1': '20.00',
           'st_tefferr2': '-20.00', 'st_tefflim': '0', 'st_mass': '2.20', 'st_masserr1': '0.10', 'st_masserr2': '-0.20',
           'st_masslim': '0', 'st_rad': '11.00', 'st_raderr1': '1.00', 'st_raderr2': '-1.00', 'st_radlim': '0',
           'rowupdate': '2014-05-14', 'pl_facility': 'Okayama Astrophysical Observatory'}

planet4 = {'loc_rowid': '4', 'pl_hostname': '14 Her', 'pl_name': '14 Her b', 'pl_discmethod': 'Radial Velocity',
           'pl_pnum': 1.0, 'pl_orbper': 1773.40002, 'pl_orbpererr1': '2.50000000', 'pl_orbpererr2': '-2.50000000',
           'pl_orbperlim': '0', 'pl_orbsmax': 2.93, 'pl_orbsmaxerr1': '0.080000', 'pl_orbsmaxerr2': '-0.080000',
           'pl_orbsmaxlim': '0', 'pl_orbeccen': 0.37, 'pl_orbeccenerr1': '0.000000', 'pl_orbeccenerr2': '0.000000',
           'pl_orbeccenlim': '0', 'pl_bmassj': '4.66000', 'pl_bmassjerr1': '0.15000', 'pl_bmassjerr2': '-0.15000',
           'pl_bmassjlim': '0', 'pl_bmassprov': 'Msini', 'pl_radj': '', 'pl_radjerr1': '', 'pl_radjerr2': '',
           'pl_radjlim': '0', 'pl_dens': '', 'pl_denserr1': '', 'pl_denserr2': '', 'pl_denslim': '0', 'pl_ttvflag': '0',
           'pl_kepflag': '0', 'pl_k2flag': '0', 'pl_nnotes': 0.0, 'st_dist': '17.94', 'st_disterr1': '0.01',
           'st_disterr2': '-0.01', 'st_distlim': '0', 'st_teff': '5338.00', 'st_tefferr1': '25.00', 'st_tefferr2': '-25.00',
           'st_tefflim': '0', 'st_mass': '0.90', 'st_masserr1': '0.04', 'st_masserr2': '-0.04', 'st_masslim': '0',
           'st_rad': '0.93', 'st_raderr1': '0.01', 'st_raderr2': '-0.01', 'st_radlim': '0', 'rowupdate': '2018-09-06',
           'pl_facility': 'W. M. Keck Observatory'}

planet5 = {'loc_rowid': '5', 'pl_hostname': '16 Cyg B', 'pl_name': '16 Cyg B b', 'pl_discmethod': 'Radial Velocity',
           'pl_pnum': 1.0, 'pl_orbper': 798.5, 'pl_orbpererr1': '1.00000000', 'pl_orbpererr2': '-1.00000000',
           'pl_orbperlim': '0', 'pl_orbsmax': 1.66, 'pl_orbsmaxerr1': '0.030000', 'pl_orbsmaxerr2': '-0.030000', 'pl_orbsmaxlim': '0',
           'pl_orbeccen': 0.68, 'pl_orbeccenerr1': '0.020000', 'pl_orbeccenerr2': '-0.020000', 'pl_orbeccenlim': '0',
           'pl_bmassj': '1.78000', 'pl_bmassjerr1': '0.08000', 'pl_bmassjerr2': '-0.08000', 'pl_bmassjlim': '0',
           'pl_bmassprov': 'Msini', 'pl_radj': '', 'pl_radjerr1': '', 'pl_radjerr2': '', 'pl_radjlim': '0', 'pl_dens': '',
           'pl_denserr1': '', 'pl_denserr2': '', 'pl_denslim': '0', 'pl_ttvflag': '0', 'pl_kepflag': '0', 'pl_k2flag': '0',
           'pl_nnotes': 0.0, 'st_dist': '21.41', 'st_disterr1': '0.23', 'st_disterr2': '-0.23', 'st_distlim': '0', 'st_teff': '5750.00',
           'st_tefferr1': '8.00', 'st_tefferr2': '-8.00', 'st_tefflim': '0', 'st_mass': '1.08', 'st_masserr1': '0.04',
           'st_masserr2': '-0.04', 'st_masslim': '0', 'st_rad': '1.13', 'st_raderr1': '0.01', 'st_raderr2': '-0.01', 'st_radlim': '0',
           'rowupdate': '2018-09-06', 'pl_facility': 'Multiple Observatories'}

planet6 = {'loc_rowid': '6', 'pl_hostname': '24 Sex', 'pl_name': '24 Sex b', 'pl_discmethod': 'Radial Velocity', 'pl_pnum': 2.0,
           'pl_orbper': 452.8, 'pl_orbpererr1': '2.10000000', 'pl_orbpererr2': '-4.50000000', 'pl_orbperlim': '0', 'pl_orbsmax': 1.333,
           'pl_orbsmaxerr1': '0.004000', 'pl_orbsmaxerr2': '-0.009000', 'pl_orbsmaxlim': '0', 'pl_orbeccen': 0.09,
           'pl_orbeccenerr1': '0.140000', 'pl_orbeccenerr2': '-0.060000', 'pl_orbeccenlim': '0', 'pl_bmassj': '1.99000',
           'pl_bmassjerr1': '0.26000', 'pl_bmassjerr2': '-0.38000', 'pl_bmassjlim': '0', 'pl_bmassprov': 'Msini', 'pl_radj': '',
           'pl_radjerr1': '', 'pl_radjerr2': '', 'pl_radjlim': '', 'pl_dens': '', 'pl_denserr1': '', 'pl_denserr2': '',
           'pl_denslim': '', 'pl_ttvflag': '0', 'pl_kepflag': '0', 'pl_k2flag': '0', 'pl_nnotes': 0.0, 'st_dist': '72.21',
           'st_disterr1': '0.68', 'st_disterr2': '-0.68', 'st_distlim': '0', 'st_teff': '5098.00', 'st_tefferr1': '44.00',
           'st_tefferr2': '-44.00', 'st_tefflim': '0', 'st_mass': '1.54', 'st_masserr1': '0.08', 'st_masserr2': '-0.08',
           'st_masslim': '0', 'st_rad': '4.90', 'st_raderr1': '0.08', 'st_raderr2': '-0.08', 'st_radlim': '0', 'rowupdate': '2014-05-14',
           'pl_facility': 'Lick Observatory'}

planet7 = {'loc_rowid': '7', 'pl_hostname': '24 Sex', 'pl_name': '24 Sex c', 'pl_discmethod': 'Radial Velocity', 'pl_pnum': 2.0,
           'pl_orbper': 883.0, 'pl_orbpererr1': '32.40000000', 'pl_orbpererr2': '-13.80000000', 'pl_orbperlim': '0', 'pl_orbsmax': 2.08,
           'pl_orbsmaxerr1': '0.050000', 'pl_orbsmaxerr2': '-0.020000', 'pl_orbsmaxlim': '0', 'pl_orbeccen': 0.29,
           'pl_orbeccenerr1': '0.160000', 'pl_orbeccenerr2': '-0.090000', 'pl_orbeccenlim': '0', 'pl_bmassj': '0.86000',
           'pl_bmassjerr1': '0.35000', 'pl_bmassjerr2': '-0.22000', 'pl_bmassjlim': '0', 'pl_bmassprov': 'Msini', 'pl_radj': '',
           'pl_radjerr1': '', 'pl_radjerr2': '', 'pl_radjlim': '', 'pl_dens': '', 'pl_denserr1': '', 'pl_denserr2': '', 'pl_denslim': '',
           'pl_ttvflag': '0', 'pl_kepflag': '0', 'pl_k2flag': '0', 'pl_nnotes': 0.0, 'st_dist': '72.21', 'st_disterr1': '0.68',
           'st_disterr2': '-0.68', 'st_distlim': '0', 'st_teff': '5098.00', 'st_tefferr1': '44.00', 'st_tefferr2': '-44.00', 'st_tefflim': '0',
           'st_mass': '1.54', 'st_masserr1': '0.08', 'st_masserr2': '-0.08', 'st_masslim': '0', 'st_rad': '4.90', 'st_raderr1': '0.08',
           'st_raderr2': '-0.08', 'st_radlim': '0', 'rowupdate': '2014-05-14', 'pl_facility': 'Lick Observatory'}

star1 = {'st_name' : "11 Com", "st_pnum" : 1, "st_planet1" : "11 Com b", "st_planet2" : "", "st_planet3" : "", "st_planet4" : "",
         "st_planet5" : "", "st_planet6" : "", "st_planet7" : "", "st_planet8" : "", "st_dist" : "993.366799293463927",
         "st_teff" : 4742, "st_mass" : 2.7, "st_rad" : 19}

star2 = {'st_name' : "11 UMi", "st_pnum" : 1 , "st_planet1" : "11 Umi b", "st_planet2" : "", "st_planet3" : "", "st_planet4" : ""
    , "st_planet5" : "", "st_planet6" : "" , "st_planet7" : "" , "st_planet8" : "", "st_dist" : "125.72478364389276",
         "st_teff" : 4213, "st_mass" : 2.78, "st_rad" : 29.79}

star3 = {'st_name' : "14 And", "st_pnum" : 1, "st_planet1" : "14 Amd b", "st_planet2" : "", "st_planet3" : "", "st_planet4" : "",
         "st_planet5" : "", "st_planet6" : "", "st_planet7" : "", "st_planet8" : "", "st_dist" : "75.592188544822534",
         "st_teff" : 4813, "st_mass" : 2.2, "st_rad" : 11}

star4 = {'st_name' : "14 Her", "st_pnum" : 1, "st_planet1" : "14 Her b", "st_planet2" : "", "st_planet3" : "", "st_planet4" : "",
         "st_planet5" : "", "st_planet6" : "", "st_planet7" : "", "st_planet8" : "", "st_dist" : "17.941613695113364",
         "st_teff" : 5338, "st_mass" : 0.90, "st_rad" : 0.93}

star5 = {'st_name' : "16 Cyg B", "st_pnum" : 1, "st_planet1" : "16 Cyg B b", "st_planet2" : "", "st_planet3" : "", "st_planet4" : "",
         "st_planet5" : "", "st_planet6" : "", "st_planet7" : "", "st_planet8" : "", "st_dist" : "21.41", "st_teff" : 5750,
         "st_mass" : 1.08, "st_rad" : 1.13}

star6 = {'st_name' : "24 Sex", "st_pnum" : 2, "st_planet1" : "24 Sex b", "st_planet2" : "24 Sex c", "st_planet3" : "", "st_planet4" : "",
         "st_planet5" : "", "st_planet6" : "", "st_planet7" : "", "st_planet8" : "", "st_dist" : "72.208512761026697", "st_teff" : 5098,
         "st_mass" : 1.54, "st_rad" : 4.9}




class BooksDataSourceTest(unittest.TestCase):
    def setUp(self):
        self.data = api.PlanetData("test_planets.csv")

    def tearDown(self):
        pass


    def test_planet(self):
        self.assertEqual(self.data.planet("11 Com b"), planet1)

    def test_planet_bad_name(self):
        self.assertRaises(ValueError, self.data.planet("12 Cyg B"))

    def test_planet_wrong_type(self):
        self.assertRaises(ValueError, self.data.planet(10))



    def test_planets_pl_name(self):
        self.assertEqual(self.data.planets(pl_name = "14"), [planet3,planet4])

    def test_planets_pl_hostname(self):
        self.assertEqual(self.data.planets(pl_hostname="24 Sex"), [planet6, planet7])

    def test_planets_pl_discmethod(self):
        self.assertEqual(self.data.planets(pl_discmethod="Radial Velocity"), [planet1, planet2, planet3, planet4, planet5, planet6, planet7])

    def test_planets_pl_pnum(self):
        self.assertEqual(self.data.planets(pl_pnum=2.0), [planet6, planet7])

    def test_planets_pl_pnummax(self):
        self.assertEqual(self.data.planets(pl_pnummax=1), [planet1, planet2, planet3, planet4, planet5])

    def test_planets_pl_pnummin(self):
        self.assertEqual(self.data.planets(pl_pnummin=1), [planet6, planet7])

    def test_planets_pl_orbper(self):
        self.assertEqual(self.data.planets(pl_orbper=300), [])

    def test_planets_pl_orbpermin(self):
        self.assertEqual(self.data.planets(pl_orbpermin=300), [planet3, planet4])

    def test_planets_pl_orbpermax(self):
        self.assertEqual(self.data.planets(pl_orbpermax=300), [planet1, planet2, planet5, planet6, planet7])

    def test_planets_pl_orbsmax(self):
        self.assertEqual(self.data.planets(pl_orbsmax=1.29), [planet1])

    def test_planets_pl_orbsmaxmax(self):
        self.assertEqual(self.data.planets(pl_orbsmaxmax="14"), [planet2, planet4, planet5, planet6, planet7])

    def test_planets_pl_orbsmaxmin(self):
        self.assertEqual(self.data.planets(pl_orbsmaxmin="14"), [planet1])

    def test_planets_pl_eccen(self):
        self.assertEqual(self.data.planets(pl_eccen=.231), [planet1])

    def test_planets_pl_eccenmin(self):
        self.assertEqual(self.data.planets(pl_eccenmin=.231), [planet4, planet5, planet7])

    def test_planets_pl_eccenmax(self):
        self.assertEqual(self.data.planets(pl_eccenmax=.231), [planet2, planet3, planet6])

    def test_planets_pl_massj(self):
        self.assertEqual(self.data.planets(pl_massj="14.74"), [planet2])

    def test_planets_pl_massjmin(self):
        self.assertEqual(self.data.planets(pl_massjmin="14"), [planet1])

    def test_planets_pl_massjmax(self):
        self.assertEqual(self.data.planets(pl_massjmax="14"), [planet3, planet4, planet5, planet6, planet7])

    def test_planets_pl_radj(self):
        self.assertEqual(self.data.planets(pl_radj="1"), [])

    def test_planets_pl_radjmax(self):
        self.assertEqual(self.data.planets(pl_radjmax="1"), [])

    def test_planets_pl_radjmin(self):
        self.assertEqual(self.data.planets(pl_radjmin="1"), [])

    def test_planets_pl_ttvflag(self):
        self.assertEqual(self.data.planets(pl_ttvflag="0"), [planet1, planet2, planet3, planet4, planet5, planet6, planet7])

    def test_planets_pl_kepflag(self):
        self.assertEqual(self.data.planets(pl_kepflag="0"), [planet1, planet2, planet3, planet4, planet5, planet6, planet7])

    def test_planets_pl_k2flag(self):
        self.assertEqual(self.data.planets(pl_k2flag="1"), [])

    def test_planets_pl_nnotes(self):
        self.assertEqual(self.data.planets(pl_nnotes=1), [])

    def test_planets_pl_facility(self):
        self.assertEqual(self.data.planets(pl_facility="Lick Observatory"), [planet6, planet7])

    def test_planets_bad_input_pl_facility(self):
        self.assertRaises(ValueError, self.data.planets(pl_facility = 10))

    def test_planets_bad_input_pl_radj(self):
        self.assertRaises(ValueError, self.data.planets(pl_radj = 10))

    def test_planets_bad_input_pl_orbpermin(self):
        self.assertRaises(ValueError, self.data.planets(pl_orbpermin = "10"))

    def test_planets_pl_facility_and_pl_massjmax(self):
        self.assertEqual(self.data.planets(pl_massjmax="14", pl_facility="Lick Observatory"), [planet6, planet7])

    def test_planets_pl_discmethod_and_pl_eccenmax(self):
        self.assertEqual(self.data.planets(pl_discmethod="Radial Velocity",pl_eccenmax=.231), [planet2, planet3, planet6])

    def test_planets_multiple_criteria(self):
        self.assertEqual(self.data.planets(pl_massjmax="14", pl_facility="Lick Observatory", pl_discmethod="Radial Velocity",pl_eccenmax=.231, pl_pnummin=1), [planet6])



    def test_compare_planet_pl_facility_discovery_method(self):
        self.assertEqual(self.data.compare_planet("pl_facility", "pl_discmethod", [planet1, planet2, planet6]),
                         (["Xinglong Station", "Thueringer Landessternwarte Tautenburg", "Lick Observatory"],
                          ["Radial Velocity","Radial Velocity","Radial Velocity"]))

    def test_compare_planet_pl_ttvflag_pl_massj(self):
        self.assertEqual(self.data.compare_planet("pl_ttvflag", "pl_massj", [planet3, planet5],
                                           (["0", "0"],["4.8", "1.78"])))

    def test_compare_planet_int_input(self):
        self.assertRaises(ValueError, self.data.compare_planet(10, "pl_massj", [planet5]))

    def test_compare_planet_not_valid_input(self):
        self.assertRaises(ValueError, self.data.compare_planet("goat", "pl_massj", [planet2]))



    def test_star(self):
        self.assertEqual(self.data.star("11 Com"), star1)

    def test_star_bad_name(self):
        self.assertRaises(ValueError, self.data.star("goat"))

    def test_star_wrong_type(self):
        self.assertRaises(ValueError, self.data.star(12))



    def test_stars_st_name(self):
        self.assertEqual(self.data.start(st_name = "e"), [star4, star6])

    def test_stars_st_pnum(self):
        self.assertEqual(self.data.start(st_pnum= 2), [star6])

    def test_stars_st_pnummin(self):
        self.assertEqual(self.data.start(st_pnummin=2), [star6])

    def test_stars_st_pnummax(self):
        self.assertEqual(self.data.start(st_pnummax=2), [star1, star2, star3, star4, star5])

    def test_stars_st_planet_1_name(self):
        self.assertEqual(self.data.start(st_planet_1_name="14 Her B"), [star4])

    def test_stars_st_dist(self):
        self.assertEqual(self.data.start(st_dist="21.41"), [star5])

    def test_stars_st_distmax(self):
        self.assertEqual(self.data.start(st_distmax="21.41"), [star4])

    def test_stars_st_distmin(self):
        self.assertEqual(self.data.start(st_distmin="21.41"), [star1, star2, star3, star6])

    def test_stars_st_teff(self):
        self.assertEqual(self.data.start(st_teff=4742), [star1])

    def test_stars_st_teffmax(self):
        self.assertEqual(self.data.start(st_teffmax=4742), [star2])

    def test_stars_st_teffmin(self):
        self.assertEqual(self.data.start(st_teffmin=4742), [star3, star4, star5, star6])

    def test_stars_st_mass(self):
        self.assertEqual(self.data.start(st_mass=2.7), [star1])

    def test_stars_st_massmax(self):
        self.assertEqual(self.data.start(st_massmax=2.7), [star3, star4, star5, star6])

    def test_stars_st_massmin(self):
        self.assertEqual(self.data.start(st_massmin=2.7), [star2])

    def test_stars_st_rad(self):
        self.assertEqual(self.data.start(st_rad=11), [star3])

    def test_stars_st_radmax(self):
        self.assertEqual(self.data.start(st_radmax=11), [star4, star5, star6])

    def test_stars_st_radmin(self):
        self.assertEqual(self.data.start(st_radmin=11), [star1, star2])

    def test_stars_bad_input_st_massmax(self):
        self.assertRaises(ValueError, self.data.start(st_massmax="goat"))

    def test_stars_bad_input_mass(self):
        self.assertRaises(ValueError, self.data.start(st_mass="2.7"))

    def test_stars_st_radmax_st_massmax(self):
        self.assertEqual(self.data.start(st_radmax=11, st_massmax = 2.7), [star4, star5, star6])

    def test_stars_st_radmax_st_pnum_st_distmax(self):
        self.assertEqual(self.data.start(st_radmax=11, st_pnum = 0, st_dist_max="21.41"), [star4])



    def test_compare_star_st_rad_st_mass(self):
        self.assertEqual(self.data.compare_star("st_rad", "st_mass", [star1, star3, star6]),
                         ([19, 11, 4.9], [2.7, 2.2, 4.9]))

    def test_compare_star_st_teff_st_mass(self):
        self.assertEqual(self.data.compare_star("st_teff", "st_mass", [star1, star3, star6]),
                         ([4742, 4813, 5098], [2.7, 2.2, 4.9]))

    def test_compare_star_int_input(self):
        self.assertRaises(ValueError, self.data.compare_star(12, "st_rad", [star3]))

    def test_comapre_star_bad_input(self):
        self.assertRaises(ValueError, self.data.compare_star("goat", "st_mass", [star5]))



if __name__ == '__main__':
    unittest.main()


