n=int(input("Enter pass:"))
seen=False
c=0
while n!=0:
    temp=n%10
    if temp==7:
        seen=True
    c+=1
    n//=10
if seen and c>=6:
    print("Strong")
else:
    print("Weak")