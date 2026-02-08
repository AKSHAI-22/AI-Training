lst=list(map(int, input().split()))
small=float("inf")
second=float("inf")
for i in lst:
    if i<small:
        second=small
        small=i
    elif i!=small and i<second:
        second=i
if second==float("inf"):
    print("No second minimum")
else:
    print("Second minimum:",second)