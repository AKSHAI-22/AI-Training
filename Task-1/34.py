num=int(input("Enter num: "))
n=num
s=0
while n>0:
    temp=n%10
    s=s+temp**3
    n//=10
if s==num:
    print("Armstrong")
else:
    print("Not Armstrong")

