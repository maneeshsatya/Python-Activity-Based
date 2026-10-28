# Case Study 2 - No.27 Advanced Numeric Pattern Generator
# Student: Maneesh Satya

n = 5
print("Pattern Generator")

# Pattern 1 - Increasing Triangle
print("\nPattern 1:")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# Pattern 2 - Reverse Number
print("\nPattern 2:")
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# Pattern 3 - Repeated Row Number
print("\nPattern 3:")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()

# Pattern 4 - Floyd-like counter using loops only
print("\nPattern 4:")
num = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(num, end=" ")
        num += 1
    print()

print("\nPattern generation completed using only loops")
