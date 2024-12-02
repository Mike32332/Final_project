class BookStore:
    def __init__(self):
        self.books = {} 
        self.cash = 1000.0  
    
    def add_book(self):
        name = input("Enter the name of the book: ")
        author = input("Enter the author of the book: ")
        price = float(input("Enter the price of the book: "))
        self.books[name] = {"Author": author, "Price": price}
        self.cash -= price * 0.9 
        print("Book '{name}' by {author} added successfully!")
    
    def sell_book(self):
        name = input("Enter the name of the book to sell: ")
        self.cash += self.books[name]["Price"]
        del self.books[name]
        print("Book '{name}' sold successfully!")
    
    def reduce_prices(self):
        for name, info in self.books.items():
            info["Price"] *= 0.98
            print("The new price of '{name}' by {Author} is: ${info['Price']:.2f}")
    
    def increase_prices(self):
        for name, info in self.books.items():
            info["Price"] *= 1.02
            print("The new price of '{name}' by {Author} is: ${info['Price']:.2f}")
    
    def show_books(self):
        if not self.books:
            print("No books in the inventory.")
        else:
            for name, info in self.books.items():
                print(f"\nBook Title: {name}\nAuthor: {info['Author']}")
                print(f"Buying Price: ${info['Price'] * 0.9:.2f}")
                print(f"Selling Price: ${info['Price']:.2f}")
        print(f"\nStore Balance: ${self.cash:.2f}")

