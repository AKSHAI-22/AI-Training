s=int(input("Enter S: "))
n=int(input("Enter N: "))
remain=s-n
if remain>=0:
    for i in range(1,n+1):
        print("Booked")
    print("Remaining seat:",remain)
else:
    print("HOUSEFULL")