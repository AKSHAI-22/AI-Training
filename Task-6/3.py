from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class CardPayment(Payment):
    def pay(self,amount):
        print("Paid",amount,"using card")

class UPIPayment(Payment):
    def pay(self,amount):
        print("Paid",amount,"using UPI")

class Checkout:
    def process(self,payment,amount):
        payment.pay(amount)

checkout = Checkout()
card = CardPayment()
upi = UPIPayment()

checkout.process(card,5000)
checkout.process(upi,2000)