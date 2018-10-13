#Authors: Owen Barnett and Katherine Sweeney


import api
import unittest


#  The planet dictionaries are very long, so I will make global variables up here for each planet

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


if __name__ == '__main__':
    unittest.main()

