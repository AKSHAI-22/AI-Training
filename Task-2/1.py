n=input("Enter n: ")
half=len(n)//2
sum1=0
sum2=0
if len(n)%2!=0:
    print("Enter even number digits")
else:
    for i in range(half):
        sum1=sum1+int(n[i])
    for j in range(half,len(n)):
        sum2=sum2+int(n[j])
if sum1==sum2:
    print("Balanced")
else:
    print("Not balanced")