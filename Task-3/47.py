lst = [("A",100),("B",90),("C",90),("D",80)]

lst.sort(key=lambda x: x[1], reverse=True)

rank = 0
prev = None

for i,(name,score) in enumerate(lst):
    if score != prev:
        rank = i + 1
    print(name, score, "Rank:", rank)
    prev = score
