char=input("Enter a character: ")
if char.isdigit():
    print("Number")
elif char.isalpha():
    print("Alphabet")
else:
    print("Special Character")