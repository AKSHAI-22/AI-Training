import random
from datetime import datetime
data = [1,2,3,4,5,6,7,8]
random.shuffle(data)
split = int(len(data) * 0.7)

train = data[:split]
test = data[split:]
print("Train:", train)
print("Test:", test)
print("Split time:", datetime.now())
