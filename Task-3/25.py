mat = [
    [1,2,3],
    [4,5,6],
    [7,8,8]
]
print(all(len(i)==len(set(i)) for i in mat))