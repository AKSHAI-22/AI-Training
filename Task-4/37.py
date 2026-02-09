preferences = {
    "A": {"B", "C"},
    "B": {"A"},
    "C": {"A"},
    "D": set(),
    "E": {"F"},
    "F": set()
}
mutual = []

for s, prefs in preferences.items():
    for p in prefs:
        if p in preferences and s in preferences[p]:
            pair = tuple(sorted((s, p)))
            if pair not in mutual:
                mutual.append(pair)
print("Mutual preferences:", mutual)
chosen = set()
for prefs in preferences.values():
    chosen = chosen.union(prefs)
isolated = []
for student in preferences:
    if student not in chosen:
        isolated.append(student)
print("Isolated students:", isolated)
