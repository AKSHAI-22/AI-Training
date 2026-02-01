num=int(input("Enter a number: "))
rev=0
while num>0:
    temp=num%10
    rev=rev*10+temp
    num//=10
if rev<2:
    print("Not Prime")
else:
    for i in range(2,int(rev**0.5)+1):
        if rev % i==0:
            print("Not Prime")
            break
    else:
        print("Prime")
