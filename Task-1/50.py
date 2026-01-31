n=int(input("Enter n: "))
d=int(input("Enter d: "))
c=0
while n!=0:
    temp=n%10
    if temp==d:
        c=c+1
    n//=10
print(c)
    