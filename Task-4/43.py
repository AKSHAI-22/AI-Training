records = [
    ("S1","A"),("S1","B"),("S2","A"),("S2","C")
]
session={}
person={}
for s,a in records:
    session[s]=session.get(s,0)+1
    person[a]=person.get(a,0)+1
multi=[]
for p in person:
    if person[p]>1:
        multi.append(p)
print(session)
print(multi)
