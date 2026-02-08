s=input().lower()
# letters=set()
# for i in s:
#     if i.isalpha():
#         letters.add(i)
# print(len(letters)==26)

print(len(set(i for i in s if i.isalpha()))==26)