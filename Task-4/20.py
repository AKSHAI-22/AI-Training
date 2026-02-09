doc1=["ai", "is", "powerful", "and", "useful"]
doc2=["ai", "is", "useful", "for", "students"]
s1=set(doc1)
s2=set(doc2)
common=s1 & s2
total=s1 | s2
similarity=len(common) / len(total)
if similarity >= 0.5:
    print("Documents are similar")
else:
    print("Documents are NOT similar")

