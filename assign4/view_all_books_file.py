def view_all_books(all_books):
  if all_books !=[]:
    for book in all_books:
      print(f"Title: {book['title']} | Author(S): {book['authors']} | ISBN: {book['isbn']}")
  else:
    print("No Book Found in Database!!")