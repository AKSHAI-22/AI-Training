students = {
    "Akshai": ["Python", "AI", "ML"],
    "Ravi": ["Python", "AI"],
    "Sneha": ["Python", "AI", "ML", "DL"]
}
mod={}
for i,j in students.items():
    mod[i]=len(j)

for i,j in mod.items():
    print(i,":",j)

# count={k:len(v) for k,v in student.item()}

top=max(mod,key=mod.get)
print("Student with maximum modules:", top)
print("Number of modules:", mod[top])