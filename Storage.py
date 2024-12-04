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
        self.name = input("Enter the name of the book to sell: ")
        self.cash += self.books[self.name]["Price"]
        del self.books[self.name]
        print("Book ", self.name," sold successfully!")

    def show_books(self):
        for a in self.books:
            print(a, self.books[a]["Author"])
            print(self.books[a]["Price"])
        
    
   
    
