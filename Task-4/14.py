passwords = [
    "Pass123!",
    "hello",
    "Admin@2024",
    "test123",
    "Welcome#1"
]

valid=[]
invalid=[]

for p in passwords:
    has_digit=False
    has_special=False
    for i in p:
        if i.isdigit():
            has_digit=True
        if not i.isalnum():
            has_special=True
    if has_digit and has_special:
        valid.append(p)
    else:
        invalid.append(p)
print(valid)
print(invalid)