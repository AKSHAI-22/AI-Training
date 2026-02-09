submissions = {
    "Akshai": [1, 2, 3],
    "Ravi": [2, 3],
    "Sneha": [1, 2, 3],
    "Kiran": [1]
}
all_assignment={1,2,3,4}

submited_all=[]
for name,a in submissions.items():
    if len(a)==len(all_assignment):
        submited_all.append(name)
print(submited_all)
no_sub=set()
for s in submissions.values():
    no_sub=no_sub.union(s)
print(all_assignment-no_sub)