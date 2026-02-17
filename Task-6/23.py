from abc import ABC, abstractmethod
class Report(ABC):
    @abstractmethod
    def generate(self):
        pass

class SalesReport(Report):
    def generate(self):
        print("Sales report generated")

class HRReport(Report):
    def generate(self):
        print("HR report generated")

reports = [SalesReport(), HRReport()]
for r in reports:
    r.generate()
