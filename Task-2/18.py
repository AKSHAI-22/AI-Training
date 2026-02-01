N=int(input("Enter Password: "))
num=N 
zero=False
if N%10 != 5:
    print("LOCKED")
else:
    while num>0:
        if num%10==0:
            zero=True
            break
        num//=10
    if zero:
        print("OPEN")
    else:
        print("LOCKED")
