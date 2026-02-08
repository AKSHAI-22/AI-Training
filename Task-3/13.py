n=int(input())
lst=[]
for i in range(n):
    t=tuple(map(int, input().split()))
    lst.append(t)
res=[]
for i in lst:
    #a=tuple(sorted(i))
    if tuple(sorted(i)) not in res:
        res.append(i)
print(res)
