from abc import ABC, abstractmethod
class Shipment(ABC):

    @abstractmethod
    def delivery_time(self):
        pass

class AirShipment(Shipment):
    def delivery_time(self):
        print("Delivery in 1 day")

class GroundShipment(Shipment):
    def delivery_time(self):
        print("Delivery in 5 days")

shipments = [AirShipment(), GroundShipment()]

for s in shipments:
    s.delivery_time()
