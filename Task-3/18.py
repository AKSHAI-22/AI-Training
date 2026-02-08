students = {
    "Ram": [80, 90, 70],
    "Sam": [85, 75, 95],
    "Tom": [60, 70, 65]
}

new={}
for name, marks in students.items():
    avg=sum(marks)/len(marks)
    new[name]=avg
print(new)