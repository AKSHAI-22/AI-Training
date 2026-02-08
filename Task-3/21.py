n=list(map(int, input().split()))
current=1
maxi=1
# for i in range(1,len(n)):
#     if n[i]==n[i-1]+1:
#         current+=1
#         maxi=max(current,maxi)
#     else:
#         current=1
# print(maxi)
    
for a,b in zip(n,n[1:]):
    current=current+1 if b==a+1 else 1
    maxi=max(maxi,current)
print(maxi)
