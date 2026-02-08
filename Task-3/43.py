records = [
    {"id":1,"name":"A"},
    {"id":2,"name":"B"},
    {"id":1,"name":"A"}
]
seen = set()
dupes = []
for r in records:
    t = tuple(sorted(r.items()))
    if t in seen:
        dupes.append(r)
    else:
        seen.add(t)
print("Duplicates:", dupes)
