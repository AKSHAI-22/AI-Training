n=int(input("Enter n: "))
pdt=1
while n>0:
    temp=n%10
    pdt*=temp
    n//=10
print(pdt)
