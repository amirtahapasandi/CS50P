amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    user_coin = int(input("Insert Coin: "))
    if user_coin in [5,10,25]:
        amount_due -= user_coin
        
change_owed = abs(amount_due)
print(f"Change Owed: {change_owed}")