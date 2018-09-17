#author katherinesweeney
#2018-09-14

import sys
import csv

def read_file(input_file):
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
    if action == "books":
        return sort_titles(books, order)
    elif action == "authors":
        return sort_authors(books, order)
    else:
        handle_error()

def make_list_of_titles(books):
    title_list = []
    for i in books:
        title_list.append(i[0])
    return title_list

def sort_titles(books, order):
    title_list = make_list_of_titles(books)
    if order == "reverse":
        reverse_list = sorted(title_list, reverse=True)
        return reverse_list
    else:
        alpha_list = sorted(title_list)
        return alpha_list

def make_list_of_authors(books):
    author_date_list = []
    for i in books:
        author_date_list.append(i[2])
    return author_date_list

def process_raw_author_data(author_date_list):
    unwanted = ["0","1","2","3","4","5","6","7","8","9","(",")","-"]
    author_list = []
    for k in author_date_list:
        new=k
        for m in unwanted:
            new = new.replace(m, "")
            new = new.replace("  "," ")
            new = new.strip()
        if (" and " or ",") in new:
            new = new.replace(", "," and ")
            new = new.split(" and ")
            for i in new:
                author_list.append(i)
        else:
            author_list.append(new)
    return author_list

def sort_authors(books, order):
    author_date_list = make_list_of_authors(books)
    author_list = process_raw_author_data(author_date_list)
    if order == "reverse":
        reverse_list = sorted(author_list, reverse=True, key=lambda x: x.split(" ")[-1]+x.split(" ")[-2])
        return reverse_list
    else:
        alpha_list = sorted(author_list, key=lambda x: x.split(" ")[-1]+x.split(" ")[-2])
        return alpha_list

def handle_error():
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