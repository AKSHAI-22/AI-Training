n=int(input("Enter n: "))
num=n
even=odd=0
while num>0:
    temp=num%10
    if temp%2==0:
        even+=1
    else:
        odd+=1
    num//=10
print(even,odd)