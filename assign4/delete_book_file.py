from save_function_file import save_all_books

def delete_book(all_books, lent_books):
    found_search_result = False

    search_item = input("Enter title or ISBN or author's name to remove: ")

    matching_books = []

    for index, book in enumerate(all_books):
        if (search_item.lower() in book["authors"].lower() or 
            search_item.lower() in book["title"].lower() or 
            search_item in book["isbn"]):
            
            found_search_result = True
            matching_books.append((index, book))
            
            print(f"{len(matching_books)}. Title: {book['title']} - Author(S): {book['authors']} - ISBN: {book['isbn']} - Price: {book['price']} - Quantity: {book['quantity']}")
            
    if not found_search_result:
        print("No book found to remove.")
        return all_books
    
    try:
        selected_index = input("Enter the serial number of the book which you want to delete: ")
        selected_index = int(selected_index)
        
        if selected_index <= 0 or selected_index > len(matching_books):
            raise IndexError

        book_index = matching_books[selected_index - 1][0]
        book_to_delete = all_books[book_index]

        # ধার দেওয়া হয়েছে কিনা চেক করা
        for lent_book in lent_books:
            if lent_book['isbn'] == book_to_delete['isbn']:
                print(f"Cannot delete '{book_to_delete['title']}' because it is currently borrowed.")
                return all_books
        
        # ধার দেওয়া না হলে মুছে ফেলা
        all_books.pop(book_index)
        save_all_books(all_books)
        print(f"'{book_to_delete['title']}' has been deleted successfully.")
        
    except (IndexError, ValueError):
        print("Invalid input. Please enter a correct serial number.")
    
    return all_books
