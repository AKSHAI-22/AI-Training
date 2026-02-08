n = int(input("Number of students: "))
students = []
for _ in range(n):
    name = input("Name: ")
    dept = input("Dept: ")
    score = int(input("Score: "))
    students.append({"name": name, "dept": dept, "score": score})
toppers = {}
for s in students:
    d = s["dept"]
    if d not in toppers or s["score"] > toppers[d]["score"]:
        toppers[d] = s
print(toppers)
