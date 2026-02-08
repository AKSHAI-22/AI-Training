n = int(input("Size: "))
mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))
p = 0
s = 0
for i in range(n):
    for j in range(n):
        if i == j:
            p += mat[i][j]
        if i + j == n - 1:
            s += mat[i][j]
print("Primary:", p)
print("Secondary:", s)
