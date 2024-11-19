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
    
