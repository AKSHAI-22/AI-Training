num=int(input("Enter num: "))
n=num
sum=0
while n>0 :
    fact=1
    temp=n%10
    for i in range(1,temp+1):
        fact*=i
    sum=sum+fact
    n//=10
if sum==num:
    print("Strong number")
else:
    print("Not strong number")