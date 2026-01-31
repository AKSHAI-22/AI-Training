n = int(input("Enter number: "))
num=n
max1 = -1
max2 = -1
while num > 0:
    d = num % 10
    if d > max1:
        max2 = max1
        max1 = d
    elif d < max1 and d > max2:
        max2 = d
    num //= 10
print(max2)
