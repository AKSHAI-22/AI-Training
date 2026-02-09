devices = {
    "D1": ["ON", "ON", "OFF", "ON"],
    "D2": ["ON", "ON", "ON"],
    "D3": ["OFF", "OFF"],
    "D4": ["ON", "ON"]
}
k=["OFF"]
lst1=[]
for device,status in devices.items():
    common=set(status)&set(k)
    if common==set(k):
        lst1.append(device)
print(lst1)

lst2=[]
for device,status in devices.items():
    if set(status)=={"ON"}:
        lst2.append(device)
print(lst2)