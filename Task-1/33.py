num=int(input("Enter a number: "))
n=num
s=0
while n>0:
    temp=n%10
    s=s*10+temp
    n//=10
if s==num:
    print("Palindrome")
else:
    print("Not a palindrome")