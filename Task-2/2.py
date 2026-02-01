bal=int(input("Enter balance: "))
withdraw=int(input("Enter amount to be withdrawn: "))
remain_bal=bal-withdraw
if withdraw % 100 == 0 and withdraw <= bal and remain_bal>=500:
    print("Success")
else:
    print("Rejected")