marks=float(input("Enter marks: "))
if marks>100 or marks<0:
    print("Invalid input")
elif marks>=80:
    print("A Grade")
elif marks>=60:
    print("B Grade")
elif marks>=40:
    print("C Grade")
else:
    print("FAIL")

