# Records, Structs, and Data Transfer Objects
# No protection against missing or extra fields or a wrong order
# dictionary
book1 = {"Title": "ABC", "publisher": "abcp", "cost": 1205}
print(book1)
book2 = {"Title": "XYZ", "publisher": "xyzp", "cost": 1550.50}
print(book2["cost"])
book2["cost"] = 580.5
book2["author"] = "Ram"
print(book2)
book2 = {"Title": "ABC", "publisher": "abcp", "cost": 1550}
print(book2)


# tuples   # No protection against missing or extra fields or a wrong order
car1 = ("red", 3812.4, True)
print(car1)
print(car1[2])
#car1[3]=45
#print(car1[3])


# custom class
class Book:
    def __init__(self, title, author, cost, publisher):
        self.title = title
        self.author = author
        self.cost = cost
        self.publisher = publisher


Book1 = Book("The Tree", "Abhiram", 2050.89, "Rani Publish")
Book2 = Book("Twilight", "stefan", 678, "JK publications")
print(Book2.title)
Book2.cost = 1290
Book2.ebook = True
print(Book2.cost)
print(Book2)


# dataclasses.dataclass
from dataclasses import dataclass
@dataclass
class Book:
    title: str
    author: str
    cost: float
    publication: str
    ebook: bool

Book1 = Book("Justice", "Rahul", 239.3, "geeta publication", True)
print(Book1)
Book1.cost = 250
Book1.place = "bangalore"
print(Book1.place)


# collections.namedtuple
from collections import namedtuple
Book = namedtuple("Book", "name author price")
Book1 = Book("Invisible", "Rajni", 542.50)
print(Book1)
print(Book1.price)
# Book1.price = 490
# Book1.ebook = True


# typing.NamedTuple
from typing import NamedTuple
class Book(NamedTuple):
    title: str
    author: str
    price: float

Book1 = Book("The lost city", "Ram", 567.89)
print(Book1)
print(Book1.price)  # accessing fields
# Book1.price = 678.5
# price(Book1.price)
# Book1.ebook = True
# print(Book1.ebook)



#struct.Struct
from struct import Struct
MyStruct = Struct("i?f")
data = MyStruct.pack(23, False,42.0)
print(data)
s =MyStruct.unpack(data)
print(s)



#types.SimpleNamespace
from types import SimpleNamespace
Book1 = SimpleNamespace(title="bookage", author="ram", price=708)
print(Book1)
print(Book1.author)  #attribute access
Book1.price=900   # mutable
print(Book1)
Book1.publisher = "Geeta publication"
print(Book1)





