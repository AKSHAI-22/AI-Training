progress = {
    "A": {"L1","L2","L3"},
    "B": {"L1"},
    "C": {"L1","L2","L3"},
    "D": {"L2"}
}

all_lessons = {"L1","L2","L3"}
full=[]
half=[]
for s, l in progress.items():
    if l==all_lessons:
        full.append(s)
    if len(l)<len(all_lessons)/2:
        half.append(s)
print(full)
print(half)
