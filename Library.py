from Storage import BookStore 

books = BookStore()

print("HELLO THIS IS YOUR BOOKSTORE")

Choice = input("A Create a book \n B Change price \n C Sell a book \n D Show your books ")

if Choice == 'A': 
    books.add_book()

if Choice == 'B': 
    print("would you like to Increse or Decrese the price?")
    Choice = input('Type I for Increse and R for Reduce')
    if Choice == 'I':
        books.increase_prices()
    if Choice == 'R':
        books.reduce_prices()

if Choice == 'C':
   books.sell_book()

if Choice == 'D':
    books.show_books()