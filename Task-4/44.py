usage = {
    "U1":[2,3],
    "U2":[5,4],
    "U3":[1]
}
limit=6
total={}
count={}

for u,v in usage.items():
    total[u]=sum(v)
    count[u]=len(v)

exceed=[]
for u in total:
    if total[u]>limit:
        exceed.append(u)

avg={}
for u in total:
    avg[u]=total[u]/count[u]
top=max(avg,key=avg.get)
print(exceed)
print(top)
