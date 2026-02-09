from collections import Counter
reviews = [
    {"review_id": 1, "sentiment": "Positive"},
    {"review_id": 2, "sentiment": "Negative"},
    {"review_id": 3, "sentiment": "Positive"},
    {"review_id": 4, "sentiment": "Neutral"},
    {"review_id": 5, "sentiment": "Positive"},
    {"review_id": 6, "sentiment": "Negative"}
]

sen_count={}
for r in reviews:
    s=r["sentiment"]
    if s not in sen_count:
        sen_count[s]=1
    else:
        sen_count[s]+=1
print(sen_count)

top=max(sen_count, key=sen_count.get)
print(top)
