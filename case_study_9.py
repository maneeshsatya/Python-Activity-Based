# Case Study 9 - No.35 Product Rating / Feedback
ratings = [5, 4, 5, 3, 4, 5, 2, 5, 4, 4]

total = 0
count = 0
five_star = 0

for r in ratings:
    total += r
    count += 1
    if r == 5:
        five_star += 1

avg = total / count
print(f"Ratings: {ratings}")
print(f"Total ratings: {count}")
print(f"Average Rating: {avg:.1f}")
print(f"5-Star count: {five_star}")

if avg >= 4.5:
    print("Product: Excellent")
elif avg >= 4.0:
    print("Product: Good")
elif avg >= 3.0:
    print("Product: Average")
else:
    print("Product: Needs Improvement")
