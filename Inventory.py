from Library import library_books as lb
from datetime import date

def Inventory():
    

    print("Welcome to the Library's Inventory System.")
    print("""
          1) View available books
          2) Search for a book
          3) Checkout a book
          4) Return a book
          5) View overdue books
          6) View most popular books
          """)

    choice = choiceFromNumberOf(6)

    if choice == 1:
        retrieveAvailable()
    elif choice == 2:
        query = input("Book to search for: ")
        searchFor(query)
    elif choice == 3:
        id = input("Book ID for checkout: ")

        

    elif choice == 4:
        pass
    elif choice == 5:
        pass
    else: 
        pass


def retrieveAvailable():
    print("\nThe Current available books: ")

    for book in lb:
        if book.available == True:
            print(f"ID: {book.id} | Title: {book.title} | Author: {book.author}")

def searchFor(query):

    print(f'Books relevant to "{query}": ')
    for book in lb:
        if book.title.lower() == query.lower() or book.genre.lower() == query.lower():
            print(f"ID: {book.id} | Title: {book.title} | Genre: {book.genre}")

def checkoutBookWith(ID):
    foundBook = False
    index = 0

    for i, book in enumerate(lb):
        if book.id == ID:
            foundBook = True
            index = i
    
    if foundBook:
        checkoutConfirmed = input(f"Book with ID {ID} found: {lb[i].title}. Confirm checkout (yes/no)?")

        if checkoutConfirmed.lower() == "yes":
            lb[i].processCheckout()
    else:
        print(f"Book with ID {ID} not found.")

def returnBookWith(ID):
    foundBook = False
    index = 0

    for i, book in enumerate(lb):
        if book.id == ID:
            foundBook = True
            index = i
    
    if foundBook:
        returnConfirmed = input(f"Book with ID {ID} found: {lb[i].title}. Confirm return (yes/no)?")

        if returnConfirmed.lower() == "yes":
            lb[i].processReturn() 
        else: 
            print(f"Book with ID {ID} not found.")    

def retrieveOverdue():

    for book in lb:
        if book.dueDate < date.today() and book.available == False:
            print(f"ID: {book.id} | Title: {book.title} | Due Date: {book.dueDate} | Available: {book.available}")

def retrievePopularBooks():



def choiceFromNumberOf(Choices):
    choice = 0
    userDoesNotHaveChoice = True

    while userDoesNotHaveChoice:
        try:
            userInput = int(input("\nEnter the number of your choice: "))

            if choice in range(1, Choices + 1):
                userDoesNotHaveChoice = False
                choice = userInput
            else:
                print(f"Please enter a choice from 1 to {Choices}")
        except:
            print("Please enter a integer for you choice.")
    
    return choice


    

if __name__ == "__main__":
    # You can use this space to test your functions
    pass