cgpa=float(input("Enter cgpa: "))
a=int(input("Enter attendance: "))
arrears=int(input("Enter arrears: "))
if cgpa>=7.0 and a >= 75 and arrears == 0:
    print("ELIGIBLE")
else:
    print("NOT ELIGIBLE")
