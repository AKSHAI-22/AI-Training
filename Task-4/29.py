deliveries = [
    ("D1", 200),
    ("D2", 150),
    ("D1", 300),
    ("D3", 400),
    ("D2", 250),
    ("D1", 100)
]

total_earnings={}
count={}
for d,e in deliveries:
    if d in total_earnings:
        total_earnings[d]+=e
        count[d]+=1
    else:
        total_earnings[d]=e
        count[d]=1
print(total_earnings)
print(count)

avg={}
for i in total_earnings:
    avg[i]=total_earnings[i]/count[i]
print(avg)

top=max(avg,key=avg.get)
print(top)