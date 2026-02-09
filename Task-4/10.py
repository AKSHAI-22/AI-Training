reservations = [
    ("A", 1),
    ("A", 2),
    ("B", 1),
    ("A", 1), 
    ("B", 3),
    ("C", 1),
    ("B", 1)   
]
res=set()
seen=set()
for i in reservations:
    if i in seen:
        res.add(i)
    else:
        seen.add(i)
print(res)

per={}
for i,j in reservations:
    if i not in per:
        per[i]=set()
    
    per[i].add(j)
for c in per:
    print(c, ":", len(per[c]))
