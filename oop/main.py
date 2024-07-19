#main.py
from book_class import BOOK
def main():
  #creating instance of book
  my_book =Book(1984,"Georg Orwell",1949)
  # Demonstrating the __str__ method
  print(__str__(my_book))
  # Demonstrating the __repr__ method
  print(__repr__(my_book))
  # Deleting a book instance to trigger __del_
  my_book.__del__(title)
