from abc import ABC, abstractmethod
class Processor(ABC):

    @abstractmethod
    def process(self):
        pass

class ImageProcessor(Processor):
    def process(self):
        print("Processing image")

class TextProcessor(Processor):
    def process(self):
        print("Processing text")

processors = [ImageProcessor(), TextProcessor()]
for p in processors:
    p.process()
