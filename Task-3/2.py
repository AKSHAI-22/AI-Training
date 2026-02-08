lst=list(map(int, input().split()))
res=[]
for i in lst:
    if lst.count(i)==1:
        res.append(i)
print(res)