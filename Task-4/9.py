scores = {
    "Akshai": [80, 85, 90],
    "Ravi": [70, 75, 72],
    "Sneha": [88, 92, 90],
    "Kiran": [60, 65, 70]
}

avg_score={}
for name,score in scores.items():
    avg=sum(score)/len(score)
    avg_score[name]=avg
print(avg_score)

total=0
for i in avg_score.values():
    total+=i
class_avg=total/len(avg_score)

ab=[]
for name,a in avg_score.items():
    if a>class_avg:
        ab.append(name)
print(ab)

