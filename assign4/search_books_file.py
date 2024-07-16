def search_books_by_title_isbn(all_books):
  
  found_search_result = False
  
  search_item = input("Enter title or ISBN of book to search books: ")
  
  for book in all_books:
    
    if search_item.lower() in book["title"].lower() or search_item in book["isbn"]:
      
      found_search_result = True
      
      print(f"Book Found: Title: {book['title']} - Author(S): {book['authors']} - ISBN: {book['isbn']} - Price: {book['price']} - Quantity: {book['quantity']}")
      
  if not found_search_result:
    print("No book Found.")
    return


def search_books_by_authors(all_books):
  
  found_search_result = False
  
  search_item = input("Enter authors' name to search books: ")
  
  for book in all_books:
    
    if search_item.lower() in book["authors"].lower():
      
      found_search_result = True
      
      print(f"Book Found: Title: {book['title']} - Author(S): {book['authors']} - ISBN: {book['isbn']} - Price: {book['price']} - Quantity: {book['quantity']}")
      
  if not found_search_result:
    print("No book Found.")
    return