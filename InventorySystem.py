from Library import library_books as lb
from datetime import date
from Book import Book
import os

# Description: a general function to display and navigate to different program functionallities.
# Notes: collectChoice() forces the user to select a choice from 1-8. Once inside a if-elif-else block 
#        the menu() call terminates with a return statement, ending further accidental function continuation.
def menu():
    print("\n\n\t     ----- MENU -----")
    print("""
          (1) View books
          (2) Search for a book
          (3) Checkout a book
          (4) Return a book
          (5) View overdue books
          (6) View popular books 
          (7) Modify a book
          (8) Register a book
          (9) Remove a book
          (10) Exit
          """)

    choice = collectChoice(10)

    os.system('clear')


    if choice == 1:
        return retrieveAvailable()
    elif choice == 2:
        query = input("Term to search for: ")
        return searchFor(query)
    elif choice == 3:
        id = input("\nID of book for checkout: ").upper()
        return checkoutBookWith(id)
    elif choice == 4:
        id = input("\nID of book for return: ").upper() 
        return returnBookWith(id)
    elif choice == 5:
        return retrieveOverdue()
    elif choice == 6:
        return retrievePopularBooks()
    elif choice == 7:
        id = input("\nID of book for modification: ").upper()
        return modifyBookWith(id)
    elif choice == 8:
        return registerBook()
    elif choice == 9:
        id = input("\nID of book to remove: ").upper()
        return removeBookWith(id)
    else:
        return print("Inventory system closed.")
        


# Description: a function to print all books or only available books.
def retrieveAvailable():
    print("Would you like to view all books or only available books?")
    print("""
          (1) All books
          (2) Available books
          """)

    choice = collectChoice(2)

    if choice == 1:
        print("\nAll books in system: ")

        for book in lb:
            print(f"ID: {book.id} | Title: {book.title} | Author: {book.author}")
    else:
        print("\nCurrent available books: ")

        for book in lb:
            if book.available == True:
                print(f"ID: {book.id} | Title: {book.title} | Author: {book.author}")


    input("\n\nPress [Enter] to return to the Menu.\n")

    os.system('clear')
    return menu()



# Description: a function to search for a given query in book titles and authors.
def searchFor(query):

    print(f'\nBooks relevant to "{query}": ')


    for book in lb:
        if query.lower() in book.title.lower() or query.lower() in book.genre.lower():
            print(f"ID: {book.id} | Title: {book.title} | Genre: {book.genre}")

    input("\n\nPress [Enter] to return to the Menu.\n")

    os.system('clear')
    return menu()



# Description: a function to checkout a book given the book's ID.
# Notes: the function uses the Book class processCheckout() meathod to perform the checkout.
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

    os.system('clear')
    return menu() 




# Description: a function to return a book given the book's ID.
# Notes: the function uses the Book class processReturn() meathod to perform the return.
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

    os.system('clear')
    return menu()     



# Description: a function to print all overdue books.
# Notes: the function uses the Book class dueDate property to determine overdue books.
def retrieveOverdue():

    print("\nCurrent overdue books:")
    for book in lb:
        if book.dueDate != None:
            if book.dueDate < date.today() and book.available == False:
                print(f"ID: {book.id} | Title: {book.title} | Due Date: {book.dueDate} | Available: {book.available}")

    input("\n\nPress [Enter] to return to the Menu.\n")

    os.system('clear')
    return menu()   


# Description: a function to print the top three checked out books.
# Notes: Key and lambda logic refrence: https://stackoverflow.com/questions/76852998/sorting-list-of-custom-class-objects-by-a-property-in-python
def retrievePopularBooks():
    descendingSortedLibraryBooks = sorted(lb, key = lambda x: x.checkouts, reverse = True)

    topThreeBooks = descendingSortedLibraryBooks[0:3] 

    print("\nTop Three Books:")
    for book in topThreeBooks:
        print(f"ID: {book.id} | Title: {book.title} | Author: {book.author} | Checkouts: {book.checkouts}")

    input("\n\nPress [Enter] to return to the Menu.\n")

    os.system('clear')
    return menu() 

# Description: a function to register new books into the inventory system.
# Notes: the functions creates a new instance of the Book class.
def registerBook():
    print("\nEnter information on the book to register.")

    ID = collectUniqueID()
    title = input("Book title: ")
    author = input("Book author: ")
    genre = input("Book genre: ")

    print("\nNote: by default new books have no due date, zero checkouts, and are available.")

    registerConfirmed = input(f'\nConfirm register for book: "{title}". (yes/no)? ')

    if registerConfirmed.lower() == 'yes':
        lb.append(Book(ID, title, author, genre, True, None, 0))

        print("\nRegister confirmed.")
        print(f"ID: {ID} | Title: {title} | Author: {author} | Genre: {genre} | Available: True | Due Date: None | Checkouts: 0")
    else: 
        print("\nRegister not confirmed.")

    input("\n\nPress [Enter] to return to the Menu.\n")

    os.system('clear')
    return menu()

# Description: a function to change a book's title, author, or genre.
def modifyBookWith(ID):
    foundBook = False
    index = 0

    for i, book in enumerate(lb):
        if book.id == ID:
            foundBook = True
            index = i
    
    if foundBook:
        print("""
              What would you like to modify?
              
              (1) Book Title
              (2) Book Author
              (3) Genre

              Note: you cannot modify a book's ID, Available, Due Date, or Checkout fields manually.
              """)

        choice = collectChoice(3)

        if choice == 1:
            newTitle = input("What is the book's new title? ")

            confirmModifyTitle = input(f'\nConfirm to change book title from "{lb[index].title}" to "{newTitle}". (yes/no)? ') 

            if confirmModifyTitle.lower() == 'yes':
                lb[index].title = newTitle
                print("\nModify confirmed.")
                print(f"ID: {ID} | Title: {lb[index].title} | Author: {lb[index].author} | Genre: {lb[index].genre}")
            else: 
                print("\nModify not confirmed")

        elif choice == 2:
            newAuthor = input("What is the book's new author? ")

            confirmModifyAuthor = input(f'\nConfirm to change book author from "{lb[index].author}" to "{newAuthor}". (yes/no)? ') 

            if confirmModifyAuthor.lower() == 'yes':
                lb[index].author = newAuthor
                print("\nModify confirmed.")
                print(f"ID: {ID} | Title: {lb[index].title} | Author: {lb[index].author} | Genre: {lb[index].genre}")
            else: 
                print("\nModify not confirmed")
        else: 
            newGenre = input("What is the book's new genre? ")

            confirmModifyGenre = input(f'\nConfirm to change book genre from "{lb[index].genre}" to "{newGenre}". (yes/no)? ') 

            if confirmModifyGenre.lower() == 'yes':
                lb[index].genre = newGenre
                print("\nModify confirmed.")
                print(f"ID: {ID} | Title: {lb[index].title} | Author: {lb[index].author} | Genre: {lb[index].genre}")
            else: 
                print("\nModify not confirmed")
    else:
        print(f"Book with ID: {ID} not found.")

    input("\n\nPress [Enter] to return to the Menu.\n")

    os.system('clear')
    return menu() 

def removeBookWith(ID):
    foundBook = False
    index = 0

    for i, book in enumerate(lb):
        if book.id == ID:
            foundBook = True
            index = i
    
    if foundBook:
        removeConfirmed = input(f'Book with ID {ID} found: "{lb[index].title}". Confirm removal (yes/no)? ')

        if removeConfirmed.lower() == "yes":
            del lb[index]

            print("\nRemoval confirmed.")
        else:
            print("\nRemoval not confirmed.")
    else: 
        print(f"Book with ID {ID} not found.")

    input("\n\nPress [Enter] to return to the Menu.\n")

    os.system('clear')
    return menu()     



# Description: a function to obtain a unique ID from the user.
def collectUniqueID(): 
    registeredIDs = [book.id for book in lb]
    doesNotHaveUniqueID = True
    ID = ""
    
    while doesNotHaveUniqueID:
        ID = input("Book ID: ").upper()

        if ID in registeredIDs:
            print("\nPlease enter a unique ID.")
        else:
            doesNotHaveUniqueID = False

    return ID



# Description: a general function to obtain a number choice from a given range.
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