attempts = {
    "Akshai": [1, 2, 3, 4],
    "Ravi": [2, 3],
    "Sneha": [1, 2, 3, 4],
    "Kiran": [3, 4]
}

all_questions = set()
for q in attempts.values():
    all_questions = all_questions.union(q)
print(all_questions)

top_stud=[]
for name,q in attempts.items():
    if set(q)==all_questions:
        top_stud.append(name)
print(top_stud)