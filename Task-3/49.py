features = {"f1":2, "f2":3, "f3":5}
total = sum(features.values())
norm = {k: v/total for k,v in features.items()}
print(norm)
