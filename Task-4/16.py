orders = [
    "Pizza",
    "Burger",
    "Pizza",
    "Pasta",
    "Burger",
    "Pizza",
    "Sandwich"
]
count = {}

for d in orders:
    if d in count:
        count[d]+=1
    else:
        count[d]=1
print(count)
max_dish=None
max_count=0
for d,m in count.items():
    if m>max_count:
        max_count=m
        max_dish=d
print(max_dish)

# print(max(count, key=count.get))

print([x for x in count if count[x]==1])