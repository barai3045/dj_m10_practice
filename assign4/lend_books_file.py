from save_function_file import save_all_books, save_lent

def lend_books(all_books, lent_books):
  
  found_search_result = False
  
  search_item = input("Enter title or ISBN or author's name to lend Book: ")
  
  matching_books = []
  
  for index, book in enumerate(all_books):
    if (search_item.lower() in book["authors"].lower() or 
        search_item.lower() in book["title"].lower() or 
        search_item in book["isbn"]):
      
      found_search_result = True
      matching_books.append((index, book))
      
      print(f"{len(matching_books)}. Title: {book['title']} - Author(S): {book['authors']} - ISBN: {book['isbn']} -Price: {book['price']} - Quantity: {book['quantity']}")
      
      
  if not found_search_result:
    print("No book found to lend.")
    return lent_books
  
  try:
    selected_index = input("Enter the serial number of book which you want to lend: ")
    selected_index = int(selected_index)
    
    if selected_index <= 0 or selected_index > len(matching_books):
      raise IndexError

    book_index = matching_books[selected_index - 1][0]
    
    
    borrower = input("Enter borrower's name: ")
    
    if int(all_books[book_index]["quantity"]) > 0:
      
      remaining_quantity = int(all_books[book_index]["quantity"]) - 1
      
      borrowed_book = all_books[book_index]["title"]
      
      book_isbn = all_books[book_index]["isbn"]
      
    
      all_books[book_index]["quantity"] = str(remaining_quantity)
      
      lent_books.append({
        "title": borrowed_book,
        "borrower": borrower,
        "isbn" : book_isbn,
      })
      
      print(f"{borrower} successfully borrowed '{borrowed_book}' book! ")
      
      save_lent(lent_books)
      save_all_books(all_books)
      
    else:
      print("Not enough books available to lend")
    
  except (IndexError, ValueError):
    print("Invalid input. Please enter a correct serial number.")

  return lent_books
