from abc import ABC, abstractmethod
class Evaluation(ABC):
    @abstractmethod
    def result(self):
        pass

class SchemeA(Evaluation):
    def result(self):
        print("Result by Scheme A")

class SchemeB(Evaluation):
    def result(self):
        print("Result by Scheme B")

schemes = [SchemeA(), SchemeB()]
for s in schemes:
    s.result()
