from Library import library_books as lb
from datetime import date

def menu():
    print("Welcome to the Library's Inventory System.")
    print("""
          (1) View available books
          (2) Search for a book
          (3) Checkout a book
          (4) Return a book
          (5) View overdue books
          (6) View most popular books
          """)

    choice = collectChoice(6)

    if choice == 1:
        retrieveAvailable()
    elif choice == 2:
        query = input("Term to search for: ")
        searchFor(query)
    elif choice == 3:
        id = input("\nBook ID for checkout: ").upper()
        checkoutBookWith(id)
    elif choice == 4:
        id = input("\nBook ID for return: ").upper() 
        returnBookWith(id)
    elif choice == 5:
        retrieveOverdue()
    elif choice == 6:
        retrievePopularBooks()

def retrieveAvailable():
    print("\nCurrent available books: ")

    for book in lb:
        if book.available == True:
            print(f"ID: {book.id} | Title: {book.title} | Author: {book.author}")

    input("\n\nPress [Enter] to return to the Menu.\n")

    return menu()

def searchFor(query):

    print(f'\nBooks relevant to "{query}": ')

    for book in lb:
        if query.lower() in book.title.lower() or query.lower() in book.genre.lower():
            print(f"ID: {book.id} | Title: {book.title} | Genre: {book.genre}")

    input("\n\nPress [Enter] to return to the Menu.\n")

    return menu()

def checkoutBookWith(ID):
    foundBook = False
    index = 0

    for i, book in enumerate(lb):
        if book.id == ID:
            foundBook = True
            index = i
    
    if foundBook:
        checkoutConfirmed = input(f'Book with ID {ID} found: "{lb[index].title}". Confirm checkout (yes/no)? ')

        if checkoutConfirmed.lower() == "yes":
            lb[index].processCheckout()
        else:
            print("\nCheckout not confirmed.")
    else:
        print(f"Book with ID: {ID} not found.")

    input("\n\nPress [Enter] to return to the Menu.\n")

    return menu() 

def returnBookWith(ID):
    foundBook = False
    index = 0

    for i, book in enumerate(lb):
        if book.id == ID:
            foundBook = True
            index = i
    
    if foundBook:
        returnConfirmed = input(f'Book with ID {ID} found: "{lb[index].title}". Confirm return (yes/no)? ')

        if returnConfirmed.lower() == "yes":
            lb[index].processReturn() 
        else:
            print("\nReturn not confirmed.")
    else: 
        print(f"Book with ID {ID} not found.")

    input("\n\nPress [Enter] to return to the Menu.\n")

    return menu()     

def retrieveOverdue():

    print("\nCurrent overdue books:")
    for book in lb:
        if book.dueDate != None:
            if book.dueDate < date.today() and book.available == False:
                print(f"ID: {book.id} | Title: {book.title} | Due Date: {book.dueDate} | Available: {book.available}")

    input("\n\nPress [Enter] to return to the Menu.\n")

    return menu()  

def retrievePopularBooks():
    checkouts = []
    indicesOfGreatestCheckouts = []

    for book in lb:
        checkouts.append(book.checkouts)

    while len(indicesOfGreatestCheckouts) < 3:
        greatestCheckout = max(checkouts) 
        indicesOfGreatestCheckouts.append(checkouts.index(greatestCheckout))
        checkouts.remove(greatestCheckout)

    print()
    for index in indicesOfGreatestCheckouts:
        print(f"ID: {lb[index].id} | Title: {lb[index].title} | Checkouts: {lb[index].checkouts}")

    input("\n\nPress [Enter] to return to the Menu.\n")

    return menu()  

    
def collectChoice(numberOfChoices):
    choice = 0
    userDoesNotHaveChoice = True

    while userDoesNotHaveChoice:
        try:
            userInput = int(input("\nEnter the number of your choice: "))

            if userInput in list(range(1, numberOfChoices + 1)):
                userDoesNotHaveChoice = False
                choice = userInput
            else:
                print(f"Please enter a choice from 1 to {numberOfChoices}")
        except:
            print("Please enter a integer for you choice.")
    
    return choice
