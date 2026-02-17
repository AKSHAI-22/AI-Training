from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def predict(self,data):
        pass

class LinearModel(Model):
    def predict(self, data):
        print("Predicting using Linear Model with data:", data)

class TreeModel(Model):
    def predict(self, data):
        print("Predicting using Decision Tree Model with data:", data)

class PredictionRunner:
    def run(self, model, data):
        model.predict(data)

runner=PredictionRunner()
linear=LinearModel()
tree=TreeModel()

runner.run(linear,[1,2,3])
runner.run(tree,[4,5,6])