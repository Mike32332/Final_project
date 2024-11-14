class Book: 
    def __init__(self, title, author, price, stock=1):
        self.title = title
        self.author = author 
        self.price = price 
        self.stock = stock 

    def __str__(self):
        return f'{self.title} by {self.author} - ${self.price} (Stock: {self.stock})'
    def increse_price(self, percentage):
