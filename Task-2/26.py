H=int(input("Enter H: "))
if H>=1 and H<=2:
    charge=H*20
    print(charge)
elif H>=3 and H<=5:
    charge=H*15
    print(charge)
elif H>5:
    charge=H*10
    print(charge)
else:
    print("INVALID")