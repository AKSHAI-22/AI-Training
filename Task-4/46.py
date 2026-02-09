cert={
"A":{"AWS","ML"},
"B":{"AWS"},
"C":{"AWS","Python"}
}

sets=list(cert.values())
common=sets[0]

for s in sets[1:]:
    common=common&s

unique=[]
for e,c in cert.items():
    others=set()
    for k,v in cert.items():
        if k!=e:
            others=others|v
    if not c<=others:
        unique.append(e)
print(common)
print(unique)
