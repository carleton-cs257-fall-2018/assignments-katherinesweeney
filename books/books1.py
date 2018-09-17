#author katherinesweeney
#2018-09-14

import sys
import csv

def read_file(input_file):
    '''
    Takes a .csv and processes each entry into a list of lists
    and throws an error if file doesn't process
    :param input_file: .csv file to be processed
    :return: list of processed .csv file entries
    '''
    try:
        books = []
        with open(input_file, newline='') as file:
            reader = csv.reader(file)
            for book_info in reader:
                books.append(book_info)
            return books
    except:
        handle_error()

def choose_sort(action, order, books):
    '''
    Takes arguments from the command line and decides which
    sort to implement
    :param action: which type of sort to be performed
    :param order: whether the sort should be lexicographic or reverse lexicographic
    :param books: list of processed .csv data
    :return: sorted list of titles or authors
    '''
    if action == "books":
        return sort_titles(books, order)
    elif action == "authors":
        return sort_authors(books, order)
    else:
        handle_error()

def make_list_of_titles(books):
    '''
    Takes processed .csv data and makes a list of titles
    :param books: list of processed .csv data
    :return: list of titles
    '''
    title_list = []
    for i in books:
        title_list.append(i[0])
    return title_list

def sort_titles(books, order):
    '''
    Sort tiles lexicographically or reverse lexicographically
    :param books: list of processed .csv data
    :param order: whether the sort should be lexicographic or reverse lexicographic
    :return: list of authors sorted lexicographically by last name
    '''
    title_list = make_list_of_titles(books)
    if order == "reverse":
        reverse_list = sorted(title_list, reverse=True)
        return reverse_list
    else:
        alpha_list = sorted(title_list)
        return alpha_list

def make_list_of_authors(books):
    '''
    Takes processed .csv data and makes a list of authors
    :param books: list of processed .csv data
    :return: list of authors with dates of birth
    '''
    author_date_list = []
    for i in books:
        author_date_list.append(i[2])
    return author_date_list

def process_raw_author_data(author_date_list):
    '''
    Further processes .csv author data to remove dates and
    multiple authors
    :param author_date_list: list of authors with dates
    :return: list of authors without dates
    '''
    author_list = []
    for k in author_date_list:
        author_no_date = remove_author_dates(k)
        if (" and " or ",") in author_no_date:
            multiple_author_list = process_multiple_authors(author_no_date)
            author_list.extend(multiple_author_list)
        else:
            author_list.append(author_no_date)
    return author_list

def remove_author_dates(author_with_date):
    '''
    Removes dates from author entry
    :param author_with_date: Author entry with date
    :return: author entry without dates
    '''
    unwanted = ["0","1","2","3","4","5","6","7","8","9","(",")","-"]
    author_no_date = author_with_date
    for m in unwanted:
        author_no_date = author_no_date.replace(m, "")
        author_no_date = author_no_date.replace("  "," ")
        author_no_date = author_no_date.strip()
    return author_no_date

def process_multiple_authors(multiple_author_entry):
    '''
    Processes multiple author entries into list of
    separated authors
    :param multiple_author_entry: single entry with multiple authors
    :return: list of each author in a multiple author set
    '''
    multiple_author_entry = multiple_author_entry.replace(", "," and ")
    multiple_author_list = multiple_author_entry.split(" and ")
    return multiple_author_list

def sort_authors(books, order):
    '''
    Sort authors lexicographically or reverse lexicographically by last name
    :param books: list of processed .csv data
    :param order: whether the sort should be lexicographic or reverse lexicographic
    :return: sorted list
    '''
    author_date_list = make_list_of_authors(books)
    author_list = process_raw_author_data(author_date_list)
    if order == "reverse":
        reverse_list = sorted(author_list, reverse=True, key=lambda x: x.split(" ")[-1]+x.split(" ")[0])
        return reverse_list
    else:
        alpha_list = sorted(author_list, key=lambda x: x.split(" ")[-1]+x.split(" ")[-2])
        return alpha_list

def handle_error():
    '''
    Prints usage statement to command line in event of error and quits program
    '''
    print("Usage: python3 books1.py input-file action [sort-direction]", file=sys.stderr)
    exit()

def main():
    input_file = sys.argv[1]
    action = sys.argv[2]
    order = sys.argv[-1]

    books = read_file(input_file)
    sorted_list = choose_sort(action, order, books)
    previous = ""
    for i in sorted_list:
        if i != previous:
            print(i)
        previous = i


if __name__== "__main__":
    main()