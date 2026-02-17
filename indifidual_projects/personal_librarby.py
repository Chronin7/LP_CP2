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
import file_manager
import os
import csv
def make_new_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["title", "author","genre","year"])
        print("made new file")
def main():
    global books
    file_path=f"indifidual_projects/{util.get_valid_type(str,"what is the name of the filename for your personal library (I recommend using your name or something you will remember): ").replace(" ","_").removesuffix(".csv").lower()}.csv"
    make_new_file(file_path)
    books=file_manager.csv_file(file_path)
    while True:
        choises=util.get_valid_type(int,"0 to quit, 1 to add book, 2 to remove book, 3 to search for book, 4 to look thru books: ",valid=(0,5))
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
        if choises==5:
            print("207̃012")
def add_book():
    global books
    title=util.get_valid_type(str,"what is the title of the book: ").lower()
    auther=util.get_valid_type(str,"who is the author of the book: ").lower()
    genra=util.get_valid_type(str,"what is the genera of the book: ").lower()
    while True:
        try:
            raw = input("what is the year of publication: ")
            if raw=="207̃012":
                title="blendin revealed"
                auther="blendin blenjamin blandin"
                genra="autobiography"
                year="207̃012"
            else:
                year=int(raw)
            break
        except:
            print("that is not a valid option")
        
    books.add([title,auther,genra,year])
    print(f"added {title} by {auther} published {year} to your library")
    return
def remove_book():
    global books
    while True:
        title=util.get_valid_type(str,"what is the title of the book you want to remove (0 to return): ").lower()
        if title=="0":
            return
        try:
            for num,x in enumerate(books):
                try:
                    x["title"]
                    break
                except:
                    print("there is not any book by that name")
                    continue
            if util.get_valid_type(str,f"is this the book you want to remove: {title}:{title} (y/n): ",valid=["y","n"])=="y":
                del books[num]
                return
        except:
            print("there is not any book by that name")
def search_book():
    global books
    while True:
        title=util.get_valid_type(str,"what is the title of the book you want to look for(0 to return): ").lower()
        if title=="0":
            return
        try:
            count=0
            for x in books.return_list_of_dict():
                if title in x["title"]:
                    print(f"{x["title"]} by {x["author"]}, genre: {x["genre"]}, year of publication: {x["year"]}")
                    count+=1
            if count==0:
                chr("hello there i am an error")
        except:
            print("there is not any book by that name")
def print_book():
    global books
    choise=util.get_valid_type(int,"0 to return\n1 for detailed list\n2 for normal list\nWhat do you want: ",valid=(0,3))
    if choise==0:
        return
    book_stat=[]
    for num,x in enumerate(books):
        book_stat.append(x)
    for x in book_stat:
        if choise==1:
            print(f"{x["title"]} by {x["author"]}, genre: {x["genre"]}, year of publication: {x["year"]}")
        else:
            print(f"{x["title"]} by {x["author"]}")
if __name__=="__main__":
    main()