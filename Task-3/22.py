n=list(map(int, input().split()))
# lst1=[]
# lst2=[]
# for i in n:
#     if i%2==0:
#         lst1.append(i)
#     else:
#         lst2.append(i)
# print(lst1)
# print(lst2)

even=[x for x in n if x%2==0]
odd=[x for x in n if x%2!=0]
print(odd)
print(even)
