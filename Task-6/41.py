from abc import ABC, abstractmethod
class Gateway(ABC):
    @abstractmethod
    def pay(self):
        pass

class PayPal(Gateway):
    def pay(self):
        print("Paid using PayPal")

class Stripe(Gateway):
    def pay(self):
        print("Paid using Stripe")

gateways = [PayPal(), Stripe()]
for g in gateways:
    g.pay()
