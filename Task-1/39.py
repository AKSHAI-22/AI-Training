num=int(input("Enter num: "))
c=0
for i in range(1,num):
    if num%i==0:
        c=c+i
if c==num:
    print("Perfect number")
else:
    print("Not a perfect number")