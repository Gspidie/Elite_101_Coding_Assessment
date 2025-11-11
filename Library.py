from Book import Book
from datetime import date

B1 = Book("B1", ",The Lightning Thief", "Rick Riordan", "Fantasy", True, None, 2)
B2 = Book("B2", "To Kill a Mockingbird", "Harper Lee", "Historical", False, date(2025, 11, 1), 5)
B3 = Book("B3", "The Great Gatsby", "F. Scott Fitzgerald", "Classic", True,  None, 3)
B4 = Book("B4", "1984", "George Orwell", "Dystopian", True, None, 4)
B5 = Book("B5", "Pride and Prejudice", "Jane Austen", "Romance",  True, None, 6)
B6 = Book("B6", "The Hobbit", "J.R.R. Tolkien", "Fantasy", False, date(2025, 11, 10), 8)
B7 = Book("B7", "Fahrenheit 451", "Ray Bradbury", "Science Fiction", True, None, 1)
B8 = Book("B8", "The Catcher in the Rye", "J.D. Salinger", "Coming-of-Age", False, date(2025, 11, 12), 3)


library_books = [B1, B2, B3, B4, B5, B6, B7, B8]
