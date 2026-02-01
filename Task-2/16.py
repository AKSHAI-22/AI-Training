n=int(input("Enter n: "))
sum=0
pdt=1
num=n
while num>0:
    temp=num%10
    sum+=temp
    pdt*=temp
    num//=10
if sum%2==0 and pdt%3==0:
    print("VALID")
else:
    print("Not VALID")