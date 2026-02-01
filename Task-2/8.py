N=int(input("Enter N: "))
min=float("inf")
for i in range(N):
    n=int(input("Enter n: "))
    if n<min:
        min=n
print(min)
