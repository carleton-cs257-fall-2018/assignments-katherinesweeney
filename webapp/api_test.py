#Authors: Owen Barnett and Katherine Sweeney


import api
import unittest

class BooksDataSourceTest(unittest.TestCase):
    def setUp(self):
        self.data = api.PlanetData("test_planets.csv")

    def tearDown(self):
        pass

'''

{host_name : "" , planet_name : "", discovery_method : "", number .... }

'''

    # def test_book(self):
    #     self.assertEqual(self.data.book(14), {'id' : 14, 'title' : 'Murder on the Orient Express', 'publication_year' : 1934})
    #
    # def test_book_not_in_set(self):
    #     self.assertRaises(ValueError, self.data.book,13)


if __name__ == '__main__':
    unittest.main()

