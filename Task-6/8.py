from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def attack(self):
        pass

class Warrior(Character):
    def attack(self):
        print("Warrior attacks with sword")

class Mage(Character):
    def attack(self):
        print("Mage attacks with magic")

characters = [Warrior(), Mage()]
for c in characters:
    c.attack()
