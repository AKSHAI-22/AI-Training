logs = [
    ("E1", "09:00"),
    ("E2", "09:05"),
    ("E1", "09:00"),
    ("E3", "09:10"),
    ("E2", "09:05"),
    ("E1", "09:15")
]
seen=set()
invalid=[]
for i in logs:
    if i in seen:
        invalid.append(i)
    else:
        seen.add(i)
print(invalid)
