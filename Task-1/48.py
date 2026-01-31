n=int(input("Enter number: "))
num=n
s=0
while num > 0:
    d = num % 10
    if d == 2 or d == 3 or d == 5 or d == 7:
        s += d
    num //= 10
print(s)
