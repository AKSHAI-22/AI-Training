nums = list(map(int, input().split()))
k = int(input())
freq = {}
for x in nums:
    freq[x] = freq.get(x, 0) + 1 
items = sorted(freq, key=freq.get, reverse=True)
print(items[:k])
