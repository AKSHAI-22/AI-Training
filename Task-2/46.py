N=int(input("Enter N: "))
for i in range(3):
    n=int(input("Enter correct pass: "))
    if n==N:
        print("Access Granted")
        break
else:
    print("Card Blocked")