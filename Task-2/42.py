w=int(input("Enter w: "))
p=int(input("Enter p: "))
price=w*p
if w>10:
    bill=price-price*(5/10)
    print(bill)
else:
    print(price)