students = [
    {"name": "Akshai", "dept": "CSE", "cgpa": 8.5},
    {"name": "Ravi", "dept": "ECE", "cgpa": 7.8},
    {"name": "Sneha", "dept": "CSE", "cgpa": 9.0},
    {"name": "Kiran", "dept": "EEE", "cgpa": 7.5},
    {"name": "Anu", "dept": "ECE", "cgpa": 8.2}
]

summary={}
for s in students:
    dept=s["dept"]
    cgpa=s["cgpa"]

    if dept not in summary:
        summary[dept]=[]
    summary[dept].append(cgpa)

new_summary={}
for s in summary:
    new_summary[s]=sum(summary[s])/len(summary[s])
print(new_summary)