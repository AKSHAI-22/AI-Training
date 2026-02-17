from abc import ABC, abstractmethod
class Delivery(ABC):
    @abstractmethod
    def deliver(self):
        pass

class BikeDelivery(Delivery):
    def deliver(self):
        print("Delivering by bike")

class TruckDelivery(Delivery):
    def deliver(self):
        print("Delivering by truck")

deliveries = [BikeDelivery(), TruckDelivery()]
for d in deliveries:
    d.deliver()
