from abc import ABC, abstractmethod

class Media(ABC):

    @abstractmethod
    def play(self):
        pass

class MP3(Media):
    def play(self):
        print("Playing MP3")

class MP4(Media):
    def play(self):
        print("Playing MP4")

media = [MP3(), MP4()]

for m in media:
    m.play()
