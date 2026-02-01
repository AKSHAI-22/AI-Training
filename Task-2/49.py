N = int(input("Enter N: "))
K = int(input("Enter K: "))
if N % K == 0:
    steps = N // K
else:
    steps = N // K + 1
print(steps)
