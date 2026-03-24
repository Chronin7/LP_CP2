#class relationship notes
#inharatance is a eg a car is a vehicle
#polymorphism
#parent class
class Vehical:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
    def move(self):
        print("move")

#child Class
class Car(Vehical):
    pass
car=Car("foord","moosetange")
print(car.brand)

class Boat(Vehical):
    def move(self):
        print("sail")
boot=Boat("nintendo","mario")
print(boot.brand)

class Clang(Vehical):
    def move(self):
        print("trust in clang")

clang=Clang("lockheed marten","f-117")




#aggragation is a HAS A eg a librarby has a book

class Librarby:
    def __init__(self,name,catolog=[]):
        self.name=name
        self.catolog=catolog
    def add_book(self,book):
        self.catolog.append(book)
    def remove_book(self,book):
        if book in self.catolog:
            self.catolog.pop(book)
    def vew_catolog(self):
        for x in self.catolog:
            print(x)
class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def __str__(self):
        return f"{self.title} by {self.author}"
    
lib=Librarby("provo")
lib.add_book(book("way of kings","braondon sandorson"))
lib.vew_catolog()


