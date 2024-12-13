from Storage import BookStore 

books = BookStore()

print("HELLO THIS IS YOUR BOOKSTORE")

while True:

    Choice = input("A Create a book \n B Sell \n C Show your books\n D show in file")

    if Choice == 'A': 
        books.add_book()


    if Choice == 'B':
        books.sell_book()

    if Choice == 'C':
        books.show_books() 

    if Choice == 'D':
        books.show_booksinfile()