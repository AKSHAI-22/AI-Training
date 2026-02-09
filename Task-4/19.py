readings = [
    {"id": 1, "temp": 30, "humidity": 60},
    {"id": 2, "temp": 32, "humidity": 58},
    {"id": 3, "temp": 31},                 
    {"id": 4, "temp": 29, "humidity": 61},
    {"id": 5, "humidity": 55}           
]
expected_keys={'id', 'humidity', 'temp'}
faulty=[]
for r in readings:
    if set(r.keys())!= expected_keys:
        faulty.append(r)
if not faulty:
    print("No fault")
else:
    for f in faulty:
        print(f)