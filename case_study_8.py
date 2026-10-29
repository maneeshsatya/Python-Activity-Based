cart = [299, 499, 150, 999]
print(f"Cart items prices: {cart}")

total = 0
for price in cart:
    total += price

print(f"Subtotal: Rs.{total}")

discount = 0
if total > 1000:
    discount = total * 0.1

final_total = total - discount

print(f"Discount (10% if >1000): Rs.{discount}")
print(f"Final Payable: Rs.{final_total}")

if final_total > 1500:
    print("Free Delivery Eligible")
else:
    print("Delivery Charges Apply: Rs.50")
