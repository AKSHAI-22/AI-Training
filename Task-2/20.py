N=int(input("Enter N:"))
digits=[0]*10
while N>0:
    temp=N%10
    digits[temp]=1
    N//=10
for i in range(10):
    if digits[i]==0:
        print(i)
        break
    