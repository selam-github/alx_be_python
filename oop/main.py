#main.py
from book_class import Book
def main():
  #creating instance of book
  my_book =Book("1984","Georg Orwell",1949)
  # Demonstrating the __str__ method
  print(__str__(my_book))
  # Demonstrating the __repr__ method
  print(repr(my_book))
  # Deleting a book instance to trigger __del_
   del my_book ()
  if __name__ == "__main__":
    main()
