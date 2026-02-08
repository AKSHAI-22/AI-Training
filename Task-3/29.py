n=int(input("How many tuples: "))
lst=[]
for i in range(n):
    t=tuple(map(int, input().split()))
    lst.append(t)
freq={}
for i in lst:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)