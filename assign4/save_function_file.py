# ফাইল Save করা      

def save_all_books(all_books):
    with open("all_books.csv", "w") as fp:
        for book in all_books:
            line = f"{book['title']},{book['authors']},{book['isbn']},{book['year']},{book['price']},{book['quantity']}\n"
            fp.write(line)


def save_lent(lent_books):
    with open("lent.csv", "w") as fp:
        for lent_book in lent_books:
            line = f"{lent_book['title']},{lent_book['borrower']},{lent_book['isbn']}\n"
            fp.write(line)
            
            