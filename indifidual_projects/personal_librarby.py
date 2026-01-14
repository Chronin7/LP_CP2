"""
import module util functions as util
books={}
define main
    set books to global
    reapeate forever 
        choies=util input int "0 to quit, 1 to add book, 2 to remove book, 3 to search for book, 4 to look thru books"
        if choises is 0
            output goodbye
            exit loop
        else if choise is 1
            add book
        else if choise is 2
            remove book
        else if choise is 3
            search book
        else if choise is 4
            ouput books
    
define output books
    set books as global
        reapeat lenght of books
            ouput books in format title : auther
    return
define serch book
    set books as global
    reapete forever
        title=util input str "what is the title of the book you want to look for (0 to return)"
        if title=0
            return
        atempt
            output title from books
            if util input str "is this your book (y/n)" =y
        if fail
            output "there is not any book with that title        
define remove book
    set books as global
    reapete forever
        title=util input str "what is the title of the book you want to remove"
        atempt
            output title from books
            if util input str "is this your book (y/n)" =y
                remove book from books
                return
        if fail
            output "there is not any book with that title
define add book
    set books as global
    title= util input str "what is the title of the book"
    auther=util input str "what is the auther of the book"
    books add tital:auther
    return
"""

import utill_functions as util
books={}
def main():
    global books
    while True:
        choises=util.get_valid_type(int,"0 to quit, 1 to add book, 2 to remove book, 3 to search for book, 4 to look thru books: ",valid=(0,4))
        if choises==0:
            print("goodbye")
            break
        if choises==1:
            add_book()
        if choises==2:
            remove_book()
        if choises==3:
            search_book()
        if choises==4:
            print_book()
def add_book():
    global books
    title=util.get_valid_type(str,"what is the title of the book: ")
    auther=util.get_valid_type(str,"who is the author of the book: ")
    books[title]=auther
    return
def remove_book():
    global books
    while True:
        title=util.get_valid_type(str,"what is the title of the book you want to remove (0 to return): ")
        if title==0:
            return
        try:
            if util.get_valid_type(str,f"is this the book you want to remove: {title}:{books[title]} (y/n): ",valid=["y","n"])=="y":
                del books[title]
                return
        except:
            print("there is not any book by that name")
def search_book():
    global books
    while True:
        title=util.get_valid_type(str,"what is the title of the book you want to look for(0 to return): ")
        if title=="0":
            return
        try:
            print(f"{title} : {books[title]}")
        except:
            print("there is not any book by that name")
def print_book():
    global books
    for x,y in books.items():
        print(f"{x} by {y}")
if __name__=="__main__":
    main()