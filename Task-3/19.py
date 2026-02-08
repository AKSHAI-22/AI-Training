def mapping(s):
    d={}
    for name,num in s.items():
        d[num]=name
    return d
students = {
    "Ram": 1,
    "Sam": 2,
    "Tom": 3
}
print(mapping(students))

# print({v: k for k, v in students.items()})
