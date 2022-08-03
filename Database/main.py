from library import *

print("""***********************************

Welcome to the Library Program.

Transactions;

1. Show Books

2. Inquire Book

3. Add Book

4. Delete Book

5. Upgrade Edition

Press 'q' to exit.
***********************************""")

library = Library()

while True:
    process = input("Process: ")

    if (process == "q"):
        print("The Program is Terminating...")
        print("Bye Bye...")
        break
    elif (process == "1"):
        library.show_books()

    elif (process == "2"):
        name = input("Book Name: ")
        print("The Book Is Questioned...")
        time.sleep(2)

        library.inquire_book(name)

    elif (process == "3"):
        name = input("Name: ")
        writer = input("Writer: ")
        publisher = input("Publisher: ")
        type = input("Type: ")
        edition = int(input("Edition: "))

        new_book = Book(name,writer,publisher,type,edition)

        print("Adding the book...")
        time.sleep(2)

        library.add_book(new_book)
        print("Added Book...")


    elif (process == "4"):
        name = input("Book Name: ")

        answer = input("OK ? (Y/N)")
        if (answer == "Y"):
            print("Deleting Book...")
            time.sleep(2)
            library.delete_book(name)
            print("Deleted Book...")


    elif (process == "5"):
        name = input("Book Name: ")
        print("Upgrading Edition....")
        time.sleep(2)
        library.upgrade_edition(name)
        print("Upgraded Edition....")

    else:
        print("Invalid Process...")