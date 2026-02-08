records = [
    {"id": 1, "name": "A"},
    {"id": 2, "name": "B"}
]
base_keys = set(records[0].keys())
consistent = True
for r in records:
    if set(r.keys()) != base_keys:
        consistent = False
        break
print("Consistent" if consistent else "Inconsistent")
