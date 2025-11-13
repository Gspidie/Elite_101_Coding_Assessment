from datetime import date, timedelta


# Description: a custom class with appropiate book properties and meathods.
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

            print("\nCheckout complete.")
            print(f"Title: {self.title} | Due Date: {self.dueDate} | Checkouts: {self.checkouts}")
        else:
            print(f"\nCheckout incomplete. Book is already checked out.")

    def processReturn(self):
        if self.available == False:
            self.available = True
            self.dueDate = None

            print("\nReturn complete.")
            print(f"Title: {self.title} | Due Date: {self.dueDate} | Available: {self.available}")
        else:
            print(f"\nReturn incomplete. Book is already available.")