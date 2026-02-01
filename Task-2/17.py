N=int(input("Enter N:"))
count=0
for i in range(1,N+1):
    num=i
    while num>0:
        if num%10==4:
            break
        num//=10
    else:
        count+=1
print(count)
