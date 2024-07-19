#main.py
from book_class import Book
def main():
  #creating instance of book
  my_book =Book(1984,"Georg Orwell",1949)
  # Demonstrating the __str__ method
  print(my_book)
  # Demonstrating the __repr__ method
  print(f"{my_book.title} by {my_book.author}, published in {my_book.year}")
  # Deleting a book instance to trigger __del_
  my_book.__del__(title)
