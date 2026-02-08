def result(lst,k):
    count=0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]==k:
                count+=1
    return count
lst=list(map(int, input("Enter numbers: ").split()))
k=int(input("Enter target: "))
print(result(lst,k))