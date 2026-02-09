slots = [
    ("Akshai", 1),
    ("Ravi", 2),
    ("Sneha", 3),
    ("Akshai", 4),   
    ("Kiran", 2)    
]
students_seen=set()
slots_seen=set()
invalid=[]
for student, slot in slots:
    if student in students_seen or slot in slots_seen:
        invalid.append((student, slot))
    else:
        students_seen.add(student)
        slots_seen.add(slot)
if invalid:
    for i in invalid:
        print(i)
else:
    print("All assignments are valid")
