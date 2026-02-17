import statistics

runs = [0.80, 0.82, 0.78, 0.81]
consistency = statistics.stdev(runs)
print("Variation across runs:", consistency)
