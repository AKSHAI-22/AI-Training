from abc import ABC, abstractmethod
class Strategy(ABC):

    @abstractmethod
    def respond(self):
        pass

class Friendly(Strategy):
    def respond(self):
        print("Hey! Nice to meet you 😊")

class Formal(Strategy):
    def respond(self):
        print("Good day. How may I assist you?")

strategies = [Friendly(), Formal()]

for s in strategies:
    s.respond()
