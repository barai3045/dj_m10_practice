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
    print("Enter Information to Add A Book: ")
    title = input("Title: ")
    authors = input("Author(s) (for multiple author use ',' comma): ").split(',')
    isbn = input("ISBN: ")
    year = input("Publishing year: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
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
            library.search_books()
        elif choice == "4":
            library.search_books_by_author()
        elif choice == "5":
            library.remove_book()
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






