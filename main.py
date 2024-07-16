from book_class import Book
from library_class import LibraryManagement
menu_text = """
    Library Management System
    1. Add Book
    2. View All Books
    3. Search Books(Title or ISBN only)
    4. Search Books by Author
    5. Remove Book
    6. Update Book
    7. Lend Book
    8. View Lent Book
    9. Return Book
    0: Exit
"""

def add_book(library):
    title = input("Enter title: ")
    authors = input("Enter authors (for multiple author use ',' comma): ").split(',')
    isbn = input("Enter ISBN: ")
    year = input("Enter publishing year: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    book = Book(title, authors, isbn, year, price, quantity)
    book.view_book()
    library.add_book(book)


def main():
    library = LibraryManagement()
    while True:
        print(menu_text)
        
        choice = input("Enter your choice: ")
        if choice =="1":
            add_book(library)
        elif choice == "2":
            library.view_all_books()
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "7":
            pass
        elif choice == "8":
            pass
        elif choice == "9":
            pass
        elif choice == "0":
            print('Thank You for Using!')
            break
        else:
            print("Invalid choice. Please choose Correct Input")



main()






