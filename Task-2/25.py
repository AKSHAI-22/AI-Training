D=int(input("Enter D: "))
if D>=1 and D<=5:
    fine=D*2
    print(fine)
elif D>5 and D<=10:
    fine=D*3
    print(fine)
elif D>10:
    fine=D*5
    print(fine)
else:
    print("INVALID")