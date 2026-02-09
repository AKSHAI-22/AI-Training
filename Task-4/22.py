passengers = [20, 35, 15, 40, 25, 10]
avg=sum(passengers)/len(passengers)
print(avg)
max_val=max(passengers)
stop=passengers.index(max_val) + 1
print(stop)

below=[]
for i in range(len(passengers)):
    if passengers[i]<avg:
        below.append(i+1)
print(below)