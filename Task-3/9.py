n=list(map(int, input().split()))
prev=None
res=[]
for i in n:
    if i!=prev:
        res.append(i)
    prev=i
print(res)