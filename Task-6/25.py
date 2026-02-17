from abc import ABC, abstractmethod
class Storage(ABC):
    @abstractmethod
    def upload(self):
        pass

class AWS(Storage):
    def upload(self):
        print("Uploaded to AWS")

class GCP(Storage):
    def upload(self):
        print("Uploaded to GCP")

stores = [AWS(), GCP()]
for s in stores:
    s.upload()
