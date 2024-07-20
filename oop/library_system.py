# library_system.py
#Base Class - Book
class Book:
    def __init__(self, title, author):
        self.title  = title
        self.author = author
    def __str__(self):
     return f"Book:{self.title} by {self.author}"
 # Derived Classes - EBook and PrintBook
class EBook(Book):
    def __init__(self,title,author,file_size):
        super().__init__(title,author) #call the base class __init__ method
        self.file_size = file_size
    def __str__(self):
        return f"EBook:{self.title} by {self.author},File Size:{self.file_size }"
class PrintBook(Book):
    def __init__(self,page_count):
     super().__init__(title,author)
     self.page_count = page_count
     def __str__(self):
         return f"PrintBook: {self.title} by {self.author} ,Page Count: {self.page_count}"

              # All the above script for inheritance
#Composition - Library
class Library:
    def __init__(self):
        self.books = []
    def add_book (self,book):
           self.books.append(book)
    def list_books(self):
        for book in self.books
        print(book)