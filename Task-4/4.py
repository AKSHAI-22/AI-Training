from collections import Counter
day1={"apple":2, "banana":3, "milk":1}
day2={"banana":2, "milk":2, "bread":1}
merged=dict(Counter(day1) + Counter(day2))
print(merged)
