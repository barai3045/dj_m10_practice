from save_function_file import save_all_books

def add_books(all_books):
    title = input("Enter Book title: ")

    while True:
        authors = input("Enter authors (Use semicolon (;) if more than 1 Author, commas are not allowed): ")
        if ',' in authors:
            print("You cannot use a comma in the authors field. use semicolon (;). Please try again.")
        else:
            break

    isbn = input("Enter ISBN: ")
    year = input("Enter publishing year: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    
    book = {
        "title": title,
        "authors": authors,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,
    }
    
    all_books.append(book)
    save_all_books(all_books)
    
    print("Books added successfully")
    
    return all_books