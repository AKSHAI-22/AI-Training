s=input()
c1,c2,c3=0,0,0
d={}
for i in s:
    if i.isdigit():
        c1+=1
    elif i.isalpha():
        c2+=1
    else:
        c3+=1
d["digits"]=c1
d["alphabets"]=c2
d["special_characters"]=c3
print(d)