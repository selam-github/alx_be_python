# library_system.py
#Base Class - Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Derived Class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

# Composition - Library
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook - Title: {book.title}, Author: {book.author}, File Size: {book.file_size} MB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook - Title: {book.title}, Author: {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book - Title: {book.title}, Author: {book.author}")

