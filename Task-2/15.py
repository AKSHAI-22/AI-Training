n=int(input("Enter n: "))
if n<0:
    print("Invalid")
elif n<1000:
    print("No discount, pay:",n)
elif n<3000:
    dis=n-n*(10/100)
    print("10% discount, pay:",dis)
elif n<5000:
    dis=n-n*(20/100)
    print("20% discount, pay:",dis)
else:
    dis=n=n*(30/100)
    print("30% discount, pay:",dis)
