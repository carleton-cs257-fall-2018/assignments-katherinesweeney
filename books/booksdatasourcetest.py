#Authors: Owen Barnett and Katherine Sweeney


import booksdatasource
import unittest

class BooksDataSourceTest(unittest.TestCase):
    def setUp(self):
        self.data = booksdatasource.BooksDataSource("test_books.csv","test_authors.csv","test_books_authors.csv")

    def tearDown(self):
        pass



    def test_book(self):
        self.assertEqual(self.data.book(14), {'id' : 14, 'title' : 'Murder on the Orient Express', 'publication_year' : 1934})

    def test_book_not_in_set(self):
        self.assertRaises(ValueError, self.data.book,13)

    def test_book_negative(self):
        self.assertRaises(ValueError, self.data.book,-27)

    def test_book_not_int(self):
        self.assertRaises(ValueError, self.data.book,"Hello, World!")



    def test_books(self):
        self.assertEqual(self.data.books(), [{'id':1,'title':'And Then There Were None', 'publication_year' : 1939},
                                             {'id':6,'title' : 'Good Omens','publication_year' : 1990},
                                             {'id': 14, 'title': 'Murder on the Orient Express','publication_year': 1934},
                                             {'id' :37,'title': 'The Fifth Season' , 'publication_year' : 2015}])

    def test_books_author_id(self):
        self.assertEqual(self.data.books(author_id=6), [{'id':6,'title' : 'Good Omens', 'publication_year' : 1990}])

    def test_books_search_text(self):
        self.assertEqual(self.data.books(search_text="on"), [{'id':1,'title':'And Then There Were None', 'publication_year' : 1939},
                                                             {'id': 14, 'title': 'Murder on the Orient Express', 'publication_year': 1934},
                                                             {'id': 37, 'title': 'The Fifth Season','publication_year': 2015}])

    def test_books_start_year(self):
        self.assertEqual(self.data.books(start_year=1940), [{'id':6,'title' : 'Good Omens','publication_year' : 1990},
                                                            {'id': 37, 'title': 'The Fifth Season', 'publication_year': 2015}])

    def test_books_end_year(self):
        self.assertEqual(self.data.books(end_year=1980), [{'id':1,'title':'And Then There Were None', 'publication_year' : 1939},
                                                          {'id': 14, 'title': 'Murder on the Orient Express', 'publication_year': 1934}])

    def test_books_sort_by(self):
        self.assertEqual(self.data.books(sort_by="year"), [{'id': 14, 'title': 'Murder on the Orient Express','publication_year': 1934},
                                                           {'id': 1, 'title': 'And Then There Were None', 'publication_year': 1939},
                                                           {'id': 6, 'title': 'Good Omens', 'publication_year': 1990},
                                                           {'id' :37,'title': 'The Fifth Season' , 'publication_year' : 2015}])

    def test_books_author_id_bad_input(self):
        self.assertRaises(ValueError, self.data.books,author_id=12)

    def test_books_search_text_bad_input(self):
        self.assertRaises(TypeError, self.data.books,search_text=12)

    def test_books_start_year_bad_input(self):
        self.assertRaises(TypeError, self.data.books,start_year="Hello, World!")

    def test_books_end_year_bad_input(self):
        self.assertRaises(TypeError, self.data.books,end_year="Hello, World!")

    def test_books_sort_by_bad_input(self):
        self.assertRaises(TypeError, self.data.books,sort_by=12)

    def test_books_two_parameters(self):
        self.assertEqual(self.data.books(start_year=1920,end_year=1950), [{'id': 1, 'title': 'And Then There Were None', 'publication_year': 1939},
                                                                          {'id': 14, 'title': 'Murder on the Orient Express','publication_year': 1934}])

    def test_books_all_parameters(self):
        self.assertEqual(self.data.books(start_year=1920,end_year=1950,search_text="a",author_id=1,sort_by="year"), [{'id': 1, 'title': 'And Then There Were None', 'publication_year': 1939}])



    def test_author(self):
        self.assertEqual(self.data.author(1), {'id': 1, 'last_name': 'Christie', 'first_name': 'Agatha', 'birth_year': 1890, 'death_year': '1976'})

    def test_author_not_in_set(self):
        self.assertRaises(ValueError, self.data.author,13)

    def test_author_negative(self):
        self.assertRaises(ValueError, self.data.author,-27)

    def test_author_not_int(self):
        self.assertRaises(ValueError, self.data.author,"Hello, World!")




    def test_authors(self):
        self.assertEqual(self.data.authors(), [{'id': 1, 'last_name': 'Christie', 'first_name': 'Agatha', 'birth_year': 1890, 'death_year': '1976'},
                                               {'id': 6, 'last_name': 'Pratchett', 'first_name': 'Terry','birth_year': 1948, 'death_year': '2015'},
                                               {'id': 5, 'last_name': 'Gaiman', 'first_name': 'Neil','birth_year': 1960, 'death_year': 'NULL'},
                                               {'id': 20, 'last_name': 'Jemisen', 'first_name': 'N.K.','birth_year': 1972, 'death_year': 'NULL'}])

    def test_authors_book_id(self):
        self.assertEqual(self.data.authors(book_id=1), [{'id': 1, 'last_name': 'Christie', 'first_name': 'Agatha', 'birth_year': 1890, 'death_year': '1976'}])

    def test_authors_search_text(self):
        self.assertEqual(self.data.authors(search_text="c"), [{'id': 1, 'last_name': 'Christie', 'first_name': 'Agatha', 'birth_year': 1890, 'death_year': '1976'},
                                                              {'id': 6, 'last_name': 'Pratchett', 'first_name': 'Terry','birth_year': 1948, 'death_year': '2015'}])

    def test_authors_start_year(self):
        self.assertEqual(self.data.authors(start_year=2016), [{'id': 5, 'last_name': 'Gaiman', 'first_name': 'Neil','birth_year': 1960, 'death_year': 'NULL'},
                                                              {'id': 20, 'last_name': 'Jemisen', 'first_name': 'N.K.', 'birth_year': 1972, 'death_year': 'NULL'}])

    def test_authors_end_year(self):
        self.assertEqual(self.data.authors(end_year=1950), [{'id': 1, 'last_name': 'Christie', 'first_name': 'Agatha', 'birth_year': 1890, 'death_year': '1976'},
                                                            {'id': 6, 'last_name': 'Pratchett', 'first_name': 'Terry','birth_year': 1948, 'death_year': '2015'}])

    def test_authors_sort_by(self):
        self.assertEqual(self.data.authors(sort_by="last_name"), [{'id': 1, 'last_name': 'Christie', 'first_name': 'Agatha', 'birth_year': 1890, 'death_year': '1976'},
                                                                  {'id': 5, 'last_name': 'Gaiman', 'first_name': 'Neil','birth_year': 1960, 'death_year': 'NULL'},
                                                                  {'id': 20, 'last_name': 'Jemisen','first_name': 'N.K.', 'birth_year': 1972,'death_year': 'NULL'},
                                                                  {'id': 6, 'last_name': 'Pratchett','first_name': 'Terry', 'birth_year': 1948,'death_year': '2015'}])

    def test_authors_book_id_bad_input(self):
        self.assertRaises(ValueError, self.data.authors,book_id=12)

    def test_authors_search_text_bad_input(self):
        self.assertRaises(TypeError, self.data.authors,search_text=12)

    def test_authors_start_year_bad_input(self):
        self.assertRaises(TypeError, self.data.authors,start_year="Hello, World!")

    def test_authors_end_year_bad_input(self):
        self.assertRaises(TypeError, self.data.authors,end_year="Hello, World!")

    def test_authors_sort_by_bad_input(self):
        self.assertRaises(TypeError, self.data.authors,sort_by=12)

    def test_authors_two_parameters(self):
        self.assertEqual(self.data.authors(start_year=1880, end_year=1920), [{'id': 1, 'last_name': 'Christie', 'first_name': 'Agatha', 'birth_year': 1890, 'death_year': '1976'}])

    def test_authors_all_parameters(self):
        self.assertEqual(self.data.authors(start_year=1880, end_year=2017, search_text="c", book_id=6, sort_by="birth_year"),[{'id': 6, 'last_name': 'Pratchett', 'first_name': 'Terry','birth_year': 1948, 'death_year': '2015'}])



    def test_books_for_author(self):
        self.assertEqual(self.data.books_for_author(1), [{'id': 1, 'title': 'And Then There Were None', 'publication_year': 1939},
                                                         {'id': 14, 'title': 'Murder on the Orient Express','publication_year': 1934}])

    def test_books_for_author_negative_int(self):
        self.assertRaises(ValueError, self.data.books_for_author,-1)

    def test_books_for_author_string(self):
        self.assertRaises(ValueError, self.data.books_for_author,"Hello, World!")



    def test_authors_for_book(self):
        self.assertEqual(self.data.authors_for_book(6), [{'id': 6, 'last_name': 'Pratchett', 'first_name': 'Terry','birth_year': 1948, 'death_year': '2015'},
                                                         {'id':5, 'last_name':'Gaiman', 'first_name':'Neil', 'birth_year':1960, 'death_year':"NULL"}])

    def test_authors_for_book_negative_int(self):
        self.assertRaises(ValueError, self.data.authors_for_book,-1)

    def test_authors_for_book_string(self):
        self.assertRaises(ValueError, self.data.authors_for_book,"Hello, World!")

if __name__ == '__main__':
    unittest.main()

