class Vechicle:
    def stop(self):
        pass

    def start(self):
        pass

class Car(Vechicle):
    def start(self):
        print("Car starts with a push button start")

    def stop(self):
        print("Car stops using hand break")

class Bike(Vechicle):
    def start(self):
        print("Bike starts with self Start")

    def stop(self):
        print("Bike stopes using breaks")

vechicles = [Car(),Bike()]
for v in vechicles:
    v.start()
    v.stop()