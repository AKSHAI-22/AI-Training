attendance = {
    "Akshai": {"Mon", "Tue", "Wed", "Thu", "Fri"},
    "Ravi": {"Mon", "Wed", "Fri"},
    "Sneha": {"Mon", "Tue", "Wed", "Thu", "Fri"},
    "Kiran": {"Tue", "Thu"}
}

working_days = {"Mon", "Tue", "Wed", "Thu", "Fri"}
total_days={}
for name,days in attendance.items():
    total_days[name]=len(days)
print(total_days)

full=[]
for name,days in attendance.items():
    if working_days==days:
        full.append(name)
print(full)