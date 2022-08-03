import sqlite3

import time

class Book():

    def __init__(self,name,writer,publisher,type,edition):

        self.name = name
        self.writer = writer
        self.publisher = publisher
        self.type = type
        self.edition = edition

    def __str__(self):

        return "Book Name: {}\nWriter: {}\nPublisher: {}\nType: {}\nEdition: {}\n".format(self.name,self.writer,self.publisher,self.type,self.edition)


class Library():

    def __init__(self):

        self.connect()

    def connect(self):

        self.connection = sqlite3.connect("C:/Workspace/Python/Projeler/Database/library.db")

        self.cursor = self.connection.cursor()

        query = "Create Table If not exists books (name TEXT,writer TEXT,publisher TEXT,type TEXT,edition INT)"

        self.cursor.execute(query)

        self.connection.commit()
    def close_connection(self):
        self.connection.close()

    def show_books(self):

        query =  "Select * From books"

        self.cursor.execute(query)

        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("There are no books in the library...")
        else:
            for i in books:

                book = Book(i[0],i[1],i[2],i[3],i[4])
                print(book)

    def inquire_book(self,name):

        query = "Select * From books where name = ?"

        self.cursor.execute(query,(name,))

        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("There is no such book...")
        else:
            book = Book(books[0][0],books[0][1],books[0][2],books[0][3],books[0][4])

            print(book)
    def add_book(self,book):

        query = "Insert into books Values(?,?,?,?,?)"

        self.cursor.execute(query,(book.name,book.writer,book.publisher,book.type,book.edition))

        self.connection.commit()

    def delete_book(self,name):

        query = "Delete From books where name = ?"

        self.cursor.execute(query,(name,))

        self.connection.commit()

    def upgrade_edition(self,name):

        query = "Select * From books where name = ?"

        self.cursor.execute(query,(name,))


        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("There is no such book...")
        else:
            edition = books[0][4]

            edition += 1

            query1 = "Update books set edition = ? where name = ?"

            self.cursor.execute(query1,(edition,name))

            self.connection.commit()



