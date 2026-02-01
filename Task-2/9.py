n=int(input("Enter n: "))
count=len(str(n))
if count==6 and n%7==0:
    print("VALID")
else:
    print("INVALID")