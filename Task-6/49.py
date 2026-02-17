import random
import statistics

data = [1,2,3,4,5,6]

sample = random.sample(data, 3)
print("Sample:", sample)
print("Mean:", statistics.mean(sample))
