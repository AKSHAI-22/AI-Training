purchases = {
    "Akshai": 4500,
    "Ravi": 6000,
    "Sneha": 12000,
    "Kiran": 8000
}

final={}
for name,amt in purchases.items():
    if amt>10000:
        pay=amt-(amt*(20/100))
    elif amt>5000:
        pay=amt-(amt*(10/100))
    else:
        pay=amt
    final[name]=pay
print(final)