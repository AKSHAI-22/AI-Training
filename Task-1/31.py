n=int(input("Enter n: "))
even=0
odd=0
for i in range(0,n+1,2):
    even+=i
for i in range(1,n+1,2):
    odd+=i
print("Sum of even numbers:",even)
print("Sum of odd numbers:",odd)