n=int(input("Enter n: "))
last_digit=n%10
if n>=3000 and last_digit==0:
    print("YES")
else:
    print("NO")