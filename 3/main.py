"""
WEEK EXERCISE
"""

# Compare conditions

a = 2
b = 330

print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are true")

if a > b or a > c:
    print("At least one of the conditions is true")

# Count the number of 'm' in 'problem solving and programming'

count = 0
for val in "problem solving and programming":
    if val != "m":
        continue
    count += 1
print("Number of 'm' in string:", count)


# What do I call this?
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print(" ")
