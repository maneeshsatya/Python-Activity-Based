# Case Study 10 - No.36 Student Result Grading System
marks = [78, 85, 90, 66, 82]
print(f"Subject Marks: {marks}")

total = 0
for m in marks:
    total += m

average = total / len(marks)
print(f"Total: {total}")
print(f"Average: {average:.2f}")

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")

if grade == "F":
    print("Result: Fail")
else:
    print("Result: Pass")
