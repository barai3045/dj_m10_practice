class Book:
    def __init__(self, title, authors, isbn, year, price, quantity, lent_to=None):
        self.title = title
        self.authors = authors
        self.isbn = isbn
        self.year = year
        self.price = price
        self.quantity = quantity
        self.lent_to = lent_to

    def view_book(self):
        return (f"\nTitle: {self.title}, Authors: {' & '.join(self.authors)}, ISBN: {self.isbn}, Year: {self.year}, Price: {self.price}, Quantity: {self.quantity}, Lent To: {self.lent_to}")
    

class Lend:
    def __init__(self, title, isbn, person):
        self.title = title
        self.isbn = isbn
        self.person = person

    def view_lend(self):
        return (f"Title: {self.title}, ISNB: {self.isbn}, Person: {self.person}")