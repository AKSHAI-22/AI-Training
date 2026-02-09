files = [
    "report.pdf",
    "photo.jpg",
    "data.csv",
    "resume.pdf",
    "image.jpg",
    "notes.txt",
    "table.csv"
]

group={}
for file in files:
    s=file.split(".")[1]

    if s not in group:
        group[s]=[]
    group[s].append(file)
print(group)