
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
        self.price = str(float(input("Enter the price of the book: ")))
        self.books[self.name] = {"Author": self.author, "Price": self.price}
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
            
   
  
    def show_booksinfile(self):
        with open("mycode.txt", "w") as file:
            for a in self.books:
                file.write("\nTitle:\n")
                file.write(a)
                file.write("\nAuthour:\n")
                file.write(self.books[a]["Author"])
                file.write("\nPrice:\n")
                file.write(self.books[a]["Price"])
                
                
                
                
            

    
