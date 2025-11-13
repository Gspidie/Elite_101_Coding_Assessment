from Book import Book
from datetime import date

# Description: a list to store Book instances.
library_books = [Book("B1", "The Lightning Thief", "Rick Riordan", "Fantasy", True, None, 2), 
                 Book("B2", "To Kill a Mockingbird", "Harper Lee", "Historical", False, date(2025, 11, 1), 5), 
                 Book("B3", "The Great Gatsby", "F. Scott Fitzgerald", "Classic", True,  None, 3), 
                 Book("B4", "1984", "George Orwell", "Dystopian", True, None, 4), 
                 Book("B5", "Pride and Prejudice", "Jane Austen", "Romance",  True, None, 6), 
                 Book("B6", "The Hobbit", "J.R.R. Tolkien", "Fantasy", False, date(2025, 11, 10), 8), 
                 Book("B7", "Fahrenheit 451", "Ray Bradbury", "Science Fiction", True, None, 1),
                 Book("B8", "The Catcher in the Rye", "J.D. Salinger", "Coming-of-Age", False, date(2025, 11, 12), 3)]