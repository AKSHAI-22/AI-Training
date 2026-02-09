employees = {
    "Akshai": {"Python", "SQL", "ML"},
    "Ravi": {"Python", "Java"},
    "Sneha": {"Python", "SQL"},
    "Kiran": {"SQL", "C++"}
}

both=[]
for name,skill in employees.items():
    if "Python" in skill and "SQL" in skill:
        both.append(name)
print(both)

all_skill=set()
for skill in employees.values():
    all_skill=all_skill | skill
print(all_skill)

skills_list = list(employees.values())
common = skills_list[0]
for s in skills_list[1:]:
    common = common & s  
print("Skills known by all:", common)
