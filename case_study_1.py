# Case Study 1 - No.13 ATM Transaction Sequence Simulation
# Student: Maneesh Satya

# Initial balance
balance = 5000
transaction_history = []
daily_withdrawal_limit = 10000
withdrawn_today = 0

# Sample transactions: (type, amount)
transactions = [
    ("deposit", 2000),
    ("withdraw", 1500),
    ("withdraw", 12000),
    ("withdraw", 3000),
    ("deposit", 500),
    ("withdraw", 1000)
]

print("ATM Transaction Simulation Started")
print(f"Initial Balance: {balance}")

for t_type, amount in transactions:
    if amount <= 0:
        print(f"Invalid amount {amount} - Rejected")
        continue

    if t_type == "deposit":
        balance += amount
        transaction_history.append((t_type, amount, "Success"))
        print(f"Deposited {amount} | New Balance: {balance}")

    elif t_type == "withdraw":
        if amount > balance:
            print(f"Withdrawal {amount} failed - Insufficient balance")
            transaction_history.append((t_type, amount, "Failed"))
        elif withdrawn_today + amount > daily_withdrawal_limit:
            print(f"Withdrawal {amount} failed - Daily limit exceeded")
            transaction_history.append((t_type, amount, "Failed"))
        else:
            balance -= amount
            withdrawn_today += amount
            transaction_history.append((t_type, amount, "Success"))
            print(f"Withdrew {amount} | New Balance: {balance}")

print("\n--- Transaction Summary ---")
for t in transaction_history:
    print(t)

print(f"\nFinal Balance: {balance}")
print(f"Total Withdrawn Today: {withdrawn_today}")
