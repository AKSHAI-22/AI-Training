a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
if a==b==c:
    print("a,b and c are largest")
elif a==b and a>c:
    print("Both a and b are larger numbers")
elif b==c and b>a:
    print("Both b and c are larger numbers")
elif a==c and a>b:
    print("Both a and c are larger numbers")
elif a>b and a>c:
    print("a is largest.")
elif b>a and b>c:
    print("b is largest")
else:
    print("c is largest")