n=int(input())
d={}
for i in range(n):
    name, value=input().split()
    d[name]=value
res = {}
for student, dept in d.items():
    if dept in res:
        res[dept].append(student)
    else:
        res[dept] = [student]
print(res)
