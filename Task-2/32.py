late=int(input("Enter lateminutes: "))
if late<0:
    print("Invalid input")
elif late<=10:
    print("Zero penalty")
elif late<=30:
    print("Penalty Rs.50")
else:
    print("Penalty Rs.100")