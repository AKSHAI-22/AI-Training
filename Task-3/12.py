def lst_num(n):
    avg=sum(n)/len(n)
    return min(n),max(n),avg
n=list(map(int, input().split()))
print(lst_num(n))
