required = {"python":3, "sql":2, "ml":4}
candidate = {"python":4, "ml":3, "html":5}

score = 0

for k in required:
    if k in candidate:
        score += required[k] * candidate[k]

print("Match score:", score)
