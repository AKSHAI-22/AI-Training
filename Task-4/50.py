papers={
"P1":["ai","ml"],
"P2":["ai","data"],
"P3":["ai","ml","data"]
}

allk=set()
sets=[]

for p,k in papers.items():
    allk=allk|set(k)
    sets.append(set(k))

common=sets[0]
for s in sets[1:]:
    common=common&s
maxp=""
m=0
for p,k in papers.items():
    if len(set(k))>m:
        m=len(set(k))
        maxp=p
print(allk)
print(common)
print(maxp)
