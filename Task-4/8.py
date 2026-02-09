temps = [
    [30, 32, 31, 29, 28, 30, 31],   # Week 1
    [33, 34, 35, 32, 31, 33, 34],   # Week 2
    [29, 28, 30, 27, 26, 28, 29]    # Week 3
]
average=[]
hot=temps[0][0]
for temp in temps:
    avg=sum(temp)/len(temp)
    average.append(f"{avg:.2f}")

    for t in temp:
        if t>hot:
            hot=t
print(f"{average}")
print(hot)

high=average[0]
week=1
for i in range(len(average)):
    if average[i]>high:
        high=average[i]
        week+=1
print(high,week)

    
