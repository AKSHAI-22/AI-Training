enrollments = {
    "Math": {"S1", "S2", "S3"},
    "Physics": {"S2", "S3", "S4"},
    "Chemistry": {"S3", "S5"},
    "Biology": {"S1", "S4"}
}
stud_count={}

for student in enrollments.values():
    for s in student:
        if s in stud_count:
            stud_count[s]+=1
        else:
            stud_count[s]=1
multi=[]
for s in stud_count:
    if stud_count[s]>1:
        multi.append(s)
print(multi)
course_sizes={}

for course, students in enrollments.items():
    course_sizes[course]=len(students)

max_size=max(course_sizes.values())

max_courses=[]
for c in course_sizes:
    if course_sizes[c]==max_size:
        max_courses.append(c)
print(max_courses)
