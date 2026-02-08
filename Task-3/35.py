n=int(input())
d={}
for i in range(n):
    name, value=input().split()
    d[name]=int(value)
# key=None
# val=-float("inf")
# for i in d:
#     if d[i]>val:
#         val=d[i]
#         key=i
# print(key)
    
print(max(d,key=d.get()))