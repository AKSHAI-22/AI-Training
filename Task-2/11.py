# n=input("Enter n: ")
# rev=n[::-1]
# sum=int(n)+int(rev)
# print(sum)

n=int(input("Enter n: "))
num=n
rev=0
while num>0:
    temp=num%10
    rev=rev*10+temp
    num//=10
print(rev)
sum=n+rev
print(sum)