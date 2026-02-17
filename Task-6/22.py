from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass

class FullTime(Employee):
    def salary(self):
        print("Full-time salary calculated")

class Contract(Employee):
    def salary(self):
        print("Contract salary calculated")

emps = [FullTime(), Contract()]
for e in emps:
    e.salary()
