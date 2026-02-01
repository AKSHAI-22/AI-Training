n=int(input("Enter n: "))
sum=0
num=n
while num>0:
    temp=num%10
    sum+=temp
    num//=10
for i in range(1,2):
    last_dig=n%10
if sum % 3 == 0 and last_dig % 2 == 0:
    print("Valid")
else:
    print("Not valid")