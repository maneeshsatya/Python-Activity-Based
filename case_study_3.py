# Case Study 3 - No.28 Repeated Transaction Detection
transactions = [101, 102, 101, 103, 104, 102, 101]
print("Checking repeated transactions...")

unique = []
repeated = []

for t in transactions:
    if t not in unique:
        unique.append(t)
    else:
        if t not in repeated:
            repeated.append(t)

print(f"All Transactions: {transactions}")
print(f"Repeated Transactions: {repeated}")
if len(repeated) > 0:
    print("Alert: Possible duplicate/fraud!")
else:
    print("No duplicates found")
