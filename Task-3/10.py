n=list(map(str, input().split()))
m=list(map(int, input().split()))

data=list(zip(n,m))
data.sort(key=lambda x: x[1],reverse=True)

rank=1
for i,j in data:
    print(i,"rank",j)
    rank+=1