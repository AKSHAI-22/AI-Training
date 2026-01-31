units=int(input("Enter units consumed:"))
if units<=100:
    bill=0
    print(bill)
elif units<=300:
    bill=(units-100)*2
    if bill>200:
        bill+=50
    print(bill)
else:
    bill=(200*2)+((units-300)*5)+100
    print(bill)