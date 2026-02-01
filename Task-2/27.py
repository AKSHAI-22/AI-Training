B=int(input("Enter B: "))
D=int(input("Enter D: "))
hr=0
if B<20:
    print("0")
elif D==0:
    print("Never")
else:
    while B>=20:
        B=B-D
        hr+=1
    print("Warning message appears in",hr,"hrs")
