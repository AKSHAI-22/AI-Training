data=[1,2,3,4,5]
remove_lst=[2,3]
result=[]
for i in data:
    if i not in remove_lst:
        result.append(i)
print(result)