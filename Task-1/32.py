num=int(input("Enter a number: "))
# while num>0:
#     temp=num%10
#     print(temp,end="")
#     num//=10
s=0
while num>0:
    temp=num%10
    s=s*10+temp
    num//=10
print(s)