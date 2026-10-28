# Case Study 7 - No.33 Attendance Reward System
attendance = [1, 1, 1, 0, 1, 1, 1, 1, 0, 1]

present = 0
total = 0
streak = 0
max_streak = 0

for a in attendance:
    total += 1
    if a == 1:
        present += 1
        streak += 1
        if streak > max_streak:
            max_streak = streak
    else:
        streak = 0

percentage = (present / total) * 100
print(f"Attendance: {attendance}")
print(f"Present: {present}/{total} = {percentage}%")
print(f"Max consecutive present: {max_streak}")

if percentage >= 75 and max_streak >= 3:
    print("Eligible for Reward")
else:
    print("Not Eligible")
