import json

class LibraryManagement:
    def __init__(self, book_file = "books.csv"):
        self.book_file = book_file
        self.books = []
        

    def load_book(self):
        try:
            with open(self.book_file, 'r') as file:
                data = json.load(file)
        
        except FileNotFoundError:
            pass
    
    def save_book(self, book):
        with open(self.book_file, 'a') as fp:
            new_book = f"{book['title']}, {book['authors']}, {book['isbn']}, {book['year']}, {book['price']}, {book['quaitity']}, {book['lent_to']}"
            fp.write(new_book)

    def add_book(self, book):
        self.books.append(book)
        self.save_book(book)

    def view_all_books(self):
        for book in self.books:
            book.view_book()

    def search_books(self, term):
        found_books = []
        for book in self.books:
            if term.lower() in book.title.lower() or term.lower() in book.isbn.lower():
                found_books.append(book)

    def search_books_by_author(self, author):
        books_by_auth = [] 
        for book in self.books:
            if author.lower() in [auth.lower() for auth in book.authors]:
                books_by_auth.append(book)

    def remove_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print("Book removed successfully.")
                return 
            print("Book book found.")

    def lend_book(self, isbn, person):
        pass

    def return_book(self, isbn):
        pass

    def view_lent_books(self):
        pass
    
