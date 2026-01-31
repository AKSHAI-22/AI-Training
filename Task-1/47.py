n=int(input("Enter n: "))
num=n
s=0
while num!=0:
    temp=num%10
    s+=temp
    num//=10
if n%s==0:
    print("Harshad number")
else:
    print("Not harshad number")