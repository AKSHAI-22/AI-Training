n=int(input("Enter n: "))
count=0
# for i in range(len(str(n+1))):
#     count=count+1
# print(count)

#print(len(str(n)))

if n==0:
    count=1
else:
    while n>0:
        count+=1
        n//=10
print(count)