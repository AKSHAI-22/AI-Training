CP=float(input("Enter Cost price: "))
SP=float(input("Enter selling price"))
if SP>CP:
    print("PROFIT")
elif SP<CP:
    print("LOSS")
else:
    print("No profit no loss")