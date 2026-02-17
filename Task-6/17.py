import statistics
scores = [70, 80, 90, 85]
avg = sum(scores) / len(scores)
variation = statistics.stdev(scores)

print("Average:", avg)
print("Variation:", variation)
