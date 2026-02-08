n = int(input("Number of students: "))
students = []
for _ in range(n):
    name = input("Name: ")
    marks = int(input("Marks: "))
    attendance = int(input("Attendance: "))
    students.append({"name": name, "marks": marks, "attendance": attendance})
performance = {}

for s in students:
    idx = s["marks"] * 0.7 + s["attendance"] * 0.3
    performance[s["name"]] = idx

print("Performance Index:", performance)
topper = max(performance, key=performance.get)
print("Topper:", topper)
