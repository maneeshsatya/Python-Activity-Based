n = 5
print("Pattern Generator")

print("\nPattern 1:")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("\nPattern 2:")
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("\nPattern 3:")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()


print("\nPattern 4:")
num = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(num, end=" ")
        num += 1
    print()

print("\nPattern generation completed using only loops")
