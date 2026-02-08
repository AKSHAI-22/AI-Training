a=list(map(int, input().split()))
b=list(map(int, input().split()))

if len(a)!=len(b):
    print("No equal length")
else:
    d=a+a
    found=False
    for i in range(len(d)):
        if d[i:i+len(a)]==b:
            found=True
            break
    print(found)