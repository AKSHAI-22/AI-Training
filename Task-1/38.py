num=int(input("Enter num: "))
c=0
for i in range(1,num+1):
    if num%i==0:
        c=c+1
print(c)