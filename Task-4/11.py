required = {"Python", "SQL", "ML", "Git"}
resumes = {
    "Akshai": ["Python", "SQL", "ML"],
    "Ravi": ["Python", "Java"],
    "Sneha": ["Python", "SQL", "ML", "Git"],
    "Kiran": ["C++", "Git"]
}

total_required = len(required)
for name, skills in resumes.items():
    skill_set=set(skills)
    matched=required&skill_set
    match_count=len(matched)
    percentage=match_count/total_required
    print("Matched skills:", matched)
    
    if percentage>=0.7:
        print("Qualified")
    else:
        print("Not Qualified")
    missing=required-skill_set
    print(missing)
