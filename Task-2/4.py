age=int(input("Enter age: "))
ticket_price=200
if age < 5:
    print("Free")
elif age>=5 and age<=12:
    final=ticket_price-ticket_price*(50/100)
    print("50% discount",final)
elif age>=13 and age<=59:
    print(ticket_price)
else:
    final=ticket_price-ticket_price*(30/100)
    print("30% Discount",final)
