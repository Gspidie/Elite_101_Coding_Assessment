from datetime import date, timedelta

class Book:
    def __init__(self, id, title, author, genre, available, dueDate, checkouts):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.dueDate = dueDate
        self.checkouts = checkouts

    def processCheckout(self):
        if self.available == True:
            self.available = False
            self.dueDate = date.today() + timedelta(weeks=2)
            self.checkouts += 1

            print("Checkout complete.")
            print(f"Checkout complete: Title: {self.title} | Due Date: {self.dueDate} | Checkouts: {self.checkouts}")
        else:
            print(f"Checkout incomplete: Book is already checked out.")

    def processReturn(self):
        self.available = True
        self.dueDate = None