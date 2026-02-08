data = [
    {"dept":"CSE","gender":"M"},
    {"dept":"ECE","gender":"F"},
    {"dept":"CSE","gender":"F"}
]
summary = {"rows": len(data), "unique_values": {}}
for key in data[0]:
    summary["unique_values"][key] = len(set(d[key] for d in data))
print(summary)
