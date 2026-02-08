n=list(map(int, input().split()))
# res=[]
# for i in range(len(n)):
#     for j in range(i+1,len(n)):
#         if n[i]<n[j]:
#             break
#     else:    
#         res.append(n[i])
# print(res)
res=[]
max_right=-float('inf')
for i in reversed(n):
    if i > max_right:
        res.append(i)
        max_right = i
print(res[::-1])
