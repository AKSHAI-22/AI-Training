transactions = [
    {"account_id": "A1", "amount": 1000, "type": "CREDIT"},
    {"account_id": "A2", "amount": 500, "type": "CREDIT"},
    {"account_id": "A1", "amount": 200, "type": "DEBIT"},
    {"account_id": "A2", "amount": 1000, "type": "CREDIT"},
    {"account_id": "A3", "amount": 700, "type": "CREDIT"},
    {"account_id": "A1", "amount": 300, "type": "CREDIT"},
    {"account_id": "A3", "amount": 200, "type": "DEBIT"}
]


bal_acc={}
for t in transactions:
    acc=t["account_id"]
    amt=t["amount"]
    if acc not in bal_acc:
        bal_acc[acc]=0
    if t["type"]=="CREDIT":
        bal_acc[acc]+=amt
    else:
        bal_acc[acc]-=amt
print(bal_acc)

top=max(bal_acc,key=bal_acc.get)
print(top)
print(bal_acc[top])