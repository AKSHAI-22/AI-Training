n=int(input())
lst=[]
for i in range(n):
    name,mark=input("Enter name and mark: ").split()
    lst.append((name,int(mark)))
lst.sort(key=lambda x:x[1],reverse=True)
print(lst)