import statistics
data = [10, 20, 30, 40, 50]

average = sum(data) / len(data)
spread = statistics.stdev(data)

print("Average:", average)
print("Spread:", spread)
