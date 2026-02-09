traffic = [
    [120, 150, 100, 130],   # Junction 1
    [200, 180, 160, 170],   # Junction 2
    [90,  110, 95,  105]    # Junction 3
]

junction_totals=[]
for t in traffic:
    junction_totals.append(sum(t))
print(junction_totals)
max_junction=junction_totals.index(max(junction_totals))+1
print(max_junction)

hours=len(traffic[0])
hour_totals=[]

for h in range(hours):
    total = 0
    for j in range(len(traffic)):
        total+=traffic[j][h]
    hour_totals.append(total)

max_hour=hour_totals.index(max(hour_totals)) + 1

print("Hour totals:", hour_totals)
print("Hour with highest traffic:", max_hour)