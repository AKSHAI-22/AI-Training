balance=int(input("Enter balance: "))
with_draw_amt=int(input("Enter amount(Must be multiple of 100) :"))
if (with_draw_amt<=balance) and (with_draw_amt%100 == 0):
    new_balance=balance-with_draw_amt
    if new_balance<500:
        print("Rejecting withdraw, Minimum blance must be greater than Rs.500")
    else:
        print("Success")
else:
    print("Withdrawal amount must be multiple of 100 AND amount must be less than balance")

