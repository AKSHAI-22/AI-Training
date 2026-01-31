price=int(input("Enter price:"))
if price<1000:
    print("No Discount!")
elif price>=1000:
    discount=price*(10/100)
    discounted_price=price-discount
    print("Discounted amount: ",discount)
    print("Final price: ",discounted_price)
elif price>=2000:
    discount=price*(20/100)
    discounted_price=price-discount
    print("Discounted amount: ",discount)
    print("Final price: ",discounted_price)
