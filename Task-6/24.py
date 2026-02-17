from abc import ABC, abstractmethod
class Workout(ABC):
    @abstractmethod
    def calories(self):
        pass

class Running(Workout):
    def calories(self):
        print("Calories from running")

class Cycling(Workout):
    def calories(self):
        print("Calories from cycling")

workouts = [Running(), Cycling()]
for w in workouts:
    w.calories()
