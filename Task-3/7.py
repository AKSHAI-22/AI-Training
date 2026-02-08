n=int(input())
matrix=[]
for i in range(n):
    n=list(map(int, input().split()))
    matrix.append(n)
print(matrix)
res=[]
for i in matrix:
    for j in i:
        res.append(j)
print(res)