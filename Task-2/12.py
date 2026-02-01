A=int(input("Enter A:"))
notes=[500,200,100,50,20,10,1]
count=0
for i in notes:
    count=count+A//i
    A=A%i
print(count)