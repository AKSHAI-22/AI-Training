sal=int(input("Enter Salary:"))
if sal<250000:
    print("No tax")
elif sal<500000:
    tax_amt=sal*(5/100)
    tsal=sal-tax_amt
    print("Tax: ",tax_amt)
    print("Salary after tax: ",tsal)
elif sal>=500000:
    tax_amt=sal*(10/100)
    tsal=sal-tax_amt
    print("Tax: ",tax_amt)
    print("Salary after tax: ",tsal)