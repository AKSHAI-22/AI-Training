records = [
    {"student": "Akshai", "book": "Python", "days": 5},
    {"student": "Ravi", "book": "AI", "days": 10},
    {"student": "Sneha", "book": "Python", "days": 8},
    {"student": "Kiran", "book": "ML", "days": 3},
    {"student": "Ravi", "book": "Python", "days": 6},
]
long_students = []
book_count = {}
for r in records:
    if r["days"] > 7 and r["student"] not in long_students:
        long_students.append(r["student"])
    book = r["book"]
    if book in book_count:
        book_count[book] += 1
    else:
        book_count[book] = 1
print("Students borrowing more than 7 days:", long_students)
print("Book borrow count:", book_count)
