L=int(input("Enter length: "))
W=int(input("Enter width: "))
H=int(input("Enter height: "))
sum=L+W+H
if L>0 and W>0 and H>0 and sum<=150:
    print("ACCEPTED")
else:
    print("REJECTED")
