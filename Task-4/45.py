inventory=[
{"product":"P1","category":"C1","stock":3},
{"product":"P2","category":"C1","stock":0},
{"product":"P3","category":"C2","stock":2}
]

out=[]
for i in inventory:
    if i["stock"]<=0:
        out.append(i["category"])
print("All stock >0:", len(out)==0)
print("Out categories:", set(out))
