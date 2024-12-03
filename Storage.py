class BookStore:
    def __init__(self):
        self.books = {} 
        self.cash = 1000.0
        self.name = ""
        self.author = "" 
        self.price = 0
    def add_book(self):
        self.name = input("Enter the name of the book: ")
        self.author = input("Enter the author of the book: ")
        self.price = float(input("Enter the price of the book: "))
        self.books[self.name] = {"Author": self.author, "Price": self.price}
        self.cash -= self.price * 0.9 
        print("Book ",self.name," by ",self.author," added successfully!")
    
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
    
    

