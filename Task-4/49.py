orders=[
{"id":1,"rest":"R1","items":["a","b"]},
{"id":2,"rest":"R2","items":[]},
{"id":3,"rest":"R1","items":["c","c"]}
]

invalid=[]
dup=[]
for o in orders:
    if not o["items"]:
        invalid.append(o["id"])
    if len(o["items"])!=len(set(o["items"])):
        dup.append(o["rest"])
print(invalid)
print(set(dup))
