experience = {
    "Akshai": [2, 1, 3],
    "Ravi": [1, 1],
    "Sneha": [3, 2, 2],
    "Kiran": [1]
}

total_experience={}
for i,t in experience.items():
    total_experience[i]=sum(t)
print(total_experience)

avg=sum(total_experience.values())/len(total_experience)
print(avg)

above=[]
for name,t in total_experience.items():
    if t>avg:
        above.append(name)
print(above)
