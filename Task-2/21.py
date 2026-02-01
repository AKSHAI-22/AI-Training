L=float(input("Enter liters: "))
P=float(input("Enter price: "))
total=int(L*P)
last_digit=total%10
if last_digit <= 4:
    total =total-last_digit
else:
    total=total+(10-last_digit)
print(total)