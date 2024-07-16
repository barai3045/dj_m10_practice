from save_function_file import save_all_books

def update_book(all_books):
    found_search_result = False

    search_item = input("Enter title or ISBN or author's name to update: ")

    matching_books = []

    for index, book in enumerate(all_books):
        if (search_item.lower() in book["authors"].lower() or 
            search_item.lower() in book["title"].lower() or 
            search_item in book["isbn"]):
            
            found_search_result = True
            matching_books.append((index, book))
            
            print(f"{len(matching_books)}. Title: {book['title']} - Author(s): {book['authors']} - ISBN: {book['isbn']} - Price: {book['price']} - Quantity: {book['quantity']}")
            
    if not found_search_result:
        print("No book found to update.")
        return all_books

    try:
        selected_index = input("Enter the serial number of the book you want to update: ")
        selected_index = int(selected_index)
        
        if selected_index <= 0 or selected_index > len(matching_books):
            raise IndexError

        book_index = matching_books[selected_index - 1][0]

        while True:
          new_authors = input("Enter authors (Use semicolon (;) if more than 1 Author, commas are not allowed): ")
          if ',' in new_authors:
            print("You cannot use a comma in the authors field. use semicolon (;). Please try again.")
          else:
            break          
        new_year = input("Enter new publishing year: ")
        new_price = float(input("Enter new price: "))
        new_quantity = int(input("Enter new quantity: "))

        all_books[book_index].update({
            "authors": new_authors,
            "year": new_year,
            "price": new_price,
            "quantity": new_quantity,
        })

        save_all_books(all_books)
        print("Book updated successfully!")

    except (IndexError, ValueError):
        print("Invalid input. Please enter a correct serial number.")
    
    return all_books
  
  