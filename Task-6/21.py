class Book:
    def __init__(self, price):
        self.__price = price

    def update_price(self, p):
        if p > 0:
            self.__price = p

    def get_price(self):
        return self.__price

b = Book(200)
b.update_price(250)
print("Price:", b.get_price())
