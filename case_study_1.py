balance, withdrawn_today = 5000, 0
limit, history = 10000, []
transactions = [("deposit", 2000), ("withdraw", 1500), ("withdraw", 12000), ("withdraw", 3000), ("deposit", 500), ("withdraw", 1000)]

print(f"ATM Transaction Simulation Started\nInitial Balance: {balance}")

for action, amt in transactions:
    if amt <= 0:
        print(f"Invalid amount {amt} - Rejected")
    elif action == "deposit":
        balance += amt
        history.append((action, amt, "Success"))
        print(f"Deposited {amt} | New Balance: {balance}")
    elif action == "withdraw":
        fail_msg = "Insufficient balance" if amt > balance else "Daily limit exceeded" if withdrawn_today + amt > limit else ""
        if fail_msg:
            print(f"Withdrawal {amt} failed - {fail_msg}")
            history.append((action, amt, "Failed"))
        else:
            balance -= amt
            withdrawn_today += amt
            history.append((action, amt, "Success"))
            print(f"Withdrew {amt} | New Balance: {balance}")

print("\n--- Transaction Summary ---")
[print(t) for t in history]
print(f"\nFinal Balance: {balance}\nTotal Withdrawn Today: {withdrawn_today}")
