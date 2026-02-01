n=int(input("Enter n: "))
num=n
sum=0
c=0
while num>0:
    temp=num%10
    c+=1
    sum=sum+temp
    num//=10
if c==4 and sum>15:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
