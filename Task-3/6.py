r=int(input())
matrix=[]
for i in range(r):
    n=list(map(int, input().split()))
    matrix.append(n)
for i in zip(*matrix):
    print(sum(i))