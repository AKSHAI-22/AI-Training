n=int(input("Enter number of sentences: "))
v=set()
for i in range(n):
    n=input().lower().split()
    for w in n:
        v.add(w)
print(v)