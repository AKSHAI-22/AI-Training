def rotate(lst,k):
    k=k%len(lst)
    lst[:]=lst[-k:]+lst[:-k]
    return lst
lst=list(map(int, input().split()))
k=int(input())
print(rotate(lst,k))