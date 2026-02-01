n=int(input("Enter n: "))
total=0
while n>0:
    temp=n%10
    if temp in[2,3,5,7]:
        total+=temp
    n//=10
print(total)

