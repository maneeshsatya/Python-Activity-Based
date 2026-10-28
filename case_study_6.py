# Case Study 6 - No.32 Character Count / Word Count
text = "Python Activity Based Learning"
print(f"Text: {text}")

vowels = "aeiouAEIOU"
v_count = 0
c_count = 0
space = 0

for ch in text:
    if ch in vowels:
        v_count += 1
    elif ch == " ":
        space += 1
    elif (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
        c_count += 1

words = space + 1

print(f"Vowels: {v_count}")
print(f"Consonants: {c_count}")
print(f"Words: {words}")
print(f"Total chars (no space): {v_count + c_count}")
