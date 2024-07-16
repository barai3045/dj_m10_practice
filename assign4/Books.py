import add_books_file
import view_all_books_file
import view_lent_books_file as view_lent_books_file
import search_books_file as search_books_file
import delete_book_file
import lend_books_file as lend_books_file
import return_books_file
import update_book_file as update_book_file


all_books =[]
lent_books = []


# all_books এর ডাটা অটো রিস্টোর করা 
def load_all_books():
  try:
    all_books.clear()
    with open("all_books.csv", "r") as fp:
      for line in fp.readlines():
        line_splitted = line.strip().split(",")
        book = {
          "title": line_splitted[0],
          "authors": line_splitted[1],
          "isbn": line_splitted[2],
          "year": line_splitted[3],
          "price": line_splitted[4],
          "quantity": line_splitted[5]
                }
        all_books.append(book)
  
  except (FileNotFoundError, ValueError):
    pass


# lent_books এর ডাটা অটো রিস্টোর করা 
def load_lent_books():
  try:
    lent_books.clear()
    with open("lent.csv", "r") as fp:
      for line in fp.readlines():
        line_splitted = line.strip().split(",")
        lent_book = {
          "title": line_splitted[0],
          "borrower": line_splitted[1],
          "isbn": line_splitted[2],
                }
        lent_books.append(lent_book)
  
  except (FileNotFoundError, ValueError):
    pass


load_all_books()
load_lent_books()

print("Welcome")

menu_text = """
Option: 
1. Add Books
2. View All Books
3. Search Books by title or ISBN
4. Search books by Authors Name
5. Update Book
6. Remove Book
7. To Lend Book
8. View Lent Books
9. Return Book
0. Exit
"""

while True:
  print(menu_text)
  menu= input("Input any number: ")
  if menu == "1":
    all_books = add_books_file.add_books(all_books)
  elif menu == "2":
    view_all_books_file.view_all_books(all_books)
  elif menu == "3":
    search_books_file.search_books_by_title_isbn(all_books)
  elif menu == "4":
    search_books_file.search_books_by_authors(all_books)
  elif menu == "5":
    all_books = update_book_file.update_book(all_books)   
  elif menu == "6":
    all_books = delete_book_file.delete_book(all_books, lent_books)
  elif menu == "7":
    lent_books = lend_books_file.lend_books(all_books, lent_books)
  elif menu == "8":
    view_lent_books_file.view_lent_books(lent_books)
  elif menu == "9":
    lent_books = return_books_file.return_books(all_books, lent_books)
  elif menu == "0":
    break
  else:
    print("Wrong Number Inputed")