bids=[("A",100),("B",200),("A",150),("C",250)]

high={}
for b,a in bids:
    if b in high:
        high[b]=max(high[b],a)
    else:
        high[b]=a

top=max(bids,key=lambda x:x[1])
print(high)
print(top)
