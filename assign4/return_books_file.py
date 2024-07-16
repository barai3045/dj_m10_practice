from save_function_file import save_all_books, save_lent

def return_books(all_books, lent_books):
  if not lent_books:
    print("No books have been lent.")
    return
  
  found_search_result = False
  search_item = input("Enter title or ISBN of the book to return: ")
  
  for index, book in enumerate(lent_books):
    if (search_item.lower() == book["title"].lower() or
        search_item == book["isbn"]):
      
      found_search_result = True
      print(f"{index+1}. Title: {book['title']} - Borrower: {book['borrower']} - ISBN: {book['isbn']}")
      
  if not found_search_result:
    print("No lent book found.")
    return  
  
  try:
    selected_index = input("Enter the serial number of the book you want to return: ")
    selected_index = int(selected_index)
    
    if selected_index <= 0 or selected_index > len(lent_books):
      raise IndexError
    
    lent_book = lent_books[selected_index - 1]
    lent_books.pop(selected_index - 1)
    
    for book in all_books:
      
      if (book["title"].lower() == lent_book["title"].lower() or
          book["isbn"] == lent_book["isbn"]):
        
        book["quantity"] = str(int(book["quantity"]) + 1)
        
        print(f"'{lent_book['title']}' successfully returned by {lent_book['borrower']}.")
        save_lent(lent_books)
        save_all_books(all_books)
        break
    
  except (IndexError, ValueError):
    print("Invalid input. Please enter a correct serial number.")
    
  return lent_books