n=int(input("Enter n: "))
d=int(input("Enter d: "))
count=0
while n!=0:
    temp=n%10
    if temp==d:
        count+=1
    n//=10
print("Count of D in N is:",count)