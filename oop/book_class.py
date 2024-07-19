#library_system.py
class Book:
    def __init__(self, title, author,year ):
     self.title = title
     self.author = author
     self.year =year
    def __del__(self):
      return f"Deleting { self.title}"
    def __str__(self):
      return f" {title} by {author} ,published {year}"
    def __repr__(self):
      return f"{self.title} by {self.author} ,published {self.year}"
