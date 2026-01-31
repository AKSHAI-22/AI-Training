a=int(input("Enter a: "))
b=int(input("Enter b: "))
if a+b>a*b:
    print("Sum is greater",a+b)
elif a+b<a*b:
    print("Product is greater",a*b)
else:
    print("Sum and Product of a&b are equal")