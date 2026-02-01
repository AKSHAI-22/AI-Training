bal = int(input("Enter balance: "))
if bal < 0:
    print("None")
elif bal < 10000:
    monthly_interest = bal * 3 / 100 / 12
    print(monthly_interest)
elif bal <= 50000:
    monthly_interest = bal * 5 / 100 / 12
    print(monthly_interest)
else:
    monthly_interest = bal * 7 / 100 / 12
    print(monthly_interest)
