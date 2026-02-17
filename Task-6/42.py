class Config:
    def __init__(self, key):
        self.__key = key

    def get_key(self):
        return self.__key

c = Config("SECRET123")
print(c.get_key())
