votes = [
    ("V1", "A"),
    ("V2", "B"),
    ("V3", "A"),
    ("V1", "C"),   
    ("V4", "B"),
    ("V2", "A")   
]
seen=set()
invalid=[]
count={}
for v,c in votes:
    if v in seen:
        invalid.append((v,c))
    else:
        seen.add(v)
        
        if c in count:
            count[c]+=1
        else:
            count[c]=1
print("Invalid votes:",invalid)
print("Final vote count:",count)
