n=int(input("Enter n: "))
sum=0
while n>0:
    temp=n%10
    sum=sum+temp
    n//=10
if sum%9==0:
    print("VAILD")
else:
    print("INVALID")