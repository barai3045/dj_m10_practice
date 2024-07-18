import csv
import json
from book_class import Book

class LibraryManagement:
    def __init__(self, book_file = "books.json", lend_file="lends.json"):
        self.book_file = book_file
        self.lend_file = lend_file
        self.books = []
        self.load_book()
        self.lends =[]
    
    def load_book(self):
        try:
            with open(self.book_file, 'r') as file:
                data = json.load(file)
                for book_data in data['books']:
                    book = Book(
                        book_data['title'], 
                        book_data['authors'], 
                        book_data['isbn'], 
                        book_data['year'], 
                        book_data['price'], 
                        book_data['quantity'], 
                        book_data['lent_to']
                        )
                    self.books.append(book)
        except FileNotFoundError:
            pass
    
    def save_data(self):
        data = {'books':[book.__dict__ for book in self.books]}
        with open(self.book_file, 'w') as fp:
            json.dump(data, fp, indent=4)

    def add_book(self, book):
        self.books.append(book)
        self.save_data()

    def save_lend(self):
        data = {'lends': [lend.__dict__ for lend in self.lends]}
        with open(self.lend_file, 'w') as fp:
            json.dump(data, fp, indent=4)

    def add_lend(self, lend):
        self.lends.append(lend)

        
    def view_all_books(self):
        for book in self.books:
            print(book.view_book())

    def search_books(self):
        term = input("Enter title or ISBN: ")
        f_books = []
        for book in self.books:
            if term.lower() in book.title.lower() or term.lower() in book.isbn.lower():
                f_books.append(book)
        
        if f_books:
            print("Search Results: ")
            for book in f_books:
                print(book.view_book())
        else:
            print("No books found.")

    def search_books_by_author(self):
        author = input("Enter author name: ")
        f_books = []
        for book in self.books:
            if author.lower() in [a.lower() for a in book.authors]:
                f_books.append(book)
        
        if f_books:
            print("Search Results: ")
            for book in f_books:
                print(book.view_book())
        else:
            print("No books found.")

    def remove_book(self):
        isbn = input("Enter ISBN: ")
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                self.save_data()
                print("Book removed successfully.")
            else:
                print("Book not found!")

    def lend_book(self, isbn, person):
        pass

    def return_book(self, isbn):
        pass

    def view_lent_books(self):
        pass
    
