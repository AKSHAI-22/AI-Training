devices={
"D1":[2,3],
"D2":[5],
"D3":[1,1]
}
total={}
for d,v in devices.items():
    total[d]=sum(v)

avg=sum(total.values())/len(total)

above=[]
for d in total:
    if total[d]>avg:
        above.append(d)
print(total)
print(above)
