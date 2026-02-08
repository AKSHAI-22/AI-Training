marks = list(map(int, input().split()))
groups = {"<50": [],"50-74": [],">=75": []}
for m in marks:
    if m < 50:
        groups["<50"].append(m)
    elif m <= 74:
        groups["50-74"].append(m)
    else:
        groups[">=75"].append(m)
print(groups)
