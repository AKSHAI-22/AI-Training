pollution = {
    "City1":[80,90],
    "City2":[120,130],
    "City3":[70,60]
}
avg={}

for c,v in pollution.items():
    avg[c]=sum(v)/len(v)
worst=max(avg, key=avg.get)
print(avg)
print(worst)
