#author katherinesweeney
#2018-09-14

import sys
import csv

def read_file(inputFile):
    try:
        books = []
        with open(inputFile, newline='') as file:
            reader = csv.reader(file)
            for bookInfo in reader:
                books.append(bookInfo)
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

def handle_error():
    print("Usage: python3 books1.py input-file action [sort-direction]", file=sys.stderr)
    exit()

def sort_titles(books, order):
    titleList = make_list_of_titles(books)
    if order == "reverse":
        reverseList = sorted(titleList, reverse=True)
        return reverseList
    else:
        alphaList = sorted(titleList)
        return alphaList

def make_list_of_titles(books):
    titleList = []
    for i in books:
        titleList.append(i[0])
    return titleList

def sort_authors(books, order):
    authorDateList = make_list_of_authors(books)
    authorList = process_raw_author_data(authorDateList)
    if order == "reverse":
        reverseList = sorted(authorList, reverse=True, key=lambda x: x.split(" ")[-1]+x.split(" ")[-2])
        return reverseList
    else:
        alphaList = sorted(authorList, key=lambda x: x.split(" ")[-1]+x.split(" ")[-2])
        return(alphaList)

def make_list_of_authors(books):
    authorDateList = []
    for i in books:
        authorDateList.append(i[2])
    return authorDateList

def process_raw_author_data(authorDateList):
    unwanted = ["0","1","2","3","4","5","6","7","8","9","(",")","-"]
    authorList = []
    for k in authorDateList:
        new=k
        for m in unwanted:
            new = new.replace(m, "")
            new = new.replace("  "," ")
            new = new.strip()
        if (" and " or ",") in new:
            new = new.replace(", "," and ")
            new = new.split(" and ")
            for i in new:
                authorList.append(i)
        else:
            authorList.append(new)
    return authorList

def main():
    inputFile = sys.argv[1]
    action = sys.argv[2]
    order = sys.argv[-1]

    books = read_file(inputFile)
    sortedList = choose_sort(action, order, books)
    previous = ""
    for i in sortedList:
        if i != previous:
            print(i)
        previous = i


if __name__== "__main__":
    main()