y=int(input("Enter y: "))
if y<0:
    print("Invalid")
elif y<2:
    print("No bonus")
elif y<=5:
    print("5000 bonus")
elif y<10:
    print("10000 bonus")
else:
    print("20000 bonus")