r = int(input("Rows: "))
matrix = []
for i in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)
for i in matrix:
    print(max(i))
