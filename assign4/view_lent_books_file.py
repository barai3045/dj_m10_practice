def view_lent_books(lent_books):
  if not lent_books:
    print("No books have been lent.")
  else:
    print("Lent Books: ")
    for book in lent_books:
      print(f"Title: {book['title']} - Borrower: {book['borrower']} - ISBN: {book['isbn']}")