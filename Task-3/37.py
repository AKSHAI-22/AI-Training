words = input("Enter words: ").split()
d={}
for w in words:
    l=len(w)
    if l in d:
        d[l].append(w)
    else:
        d[l]=[w]
print(d)