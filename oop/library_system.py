# library_system.py
# Base Class - Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

# Derived Class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook:{super().__str__()} File Size: {self.file_size} KB"

# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook:{super().__str__()} Page Count: {self.page_count}"

# Composition - Library
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only instances of Book, EBook, or PrintBook can be added.")

    def list_books(self):
        for book in self.books:
            print(book)

# Example usage
if __name__ == "__main__":
    library = Library()
    ebook = EBook("The Digital Age", "John Doe", 5)
    printbook = PrintBook("Paper Dreams", "Jane Doe", 300)
    
    library.add_book(ebook)
    library.add_book(printbook)
    
    library.list_books()
