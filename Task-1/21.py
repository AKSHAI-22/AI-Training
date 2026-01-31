a1=float(input("Enter angle 1: "))
a2=float(input("Enter angle 2: "))
a3=float(input("Enter angle 3: "))
sum=a1+a2+a3
if(a1<=0 or a2<=0 or a3<=0):
    print("Invalid triangle")
elif sum==180:
    print("Valid triangle")
else:
    print("Invalid triangle(Sum is not 180)")