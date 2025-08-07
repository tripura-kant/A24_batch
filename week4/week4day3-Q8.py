# Count how many numbers are divisible by 3 and 6 between 1 to 1000
# by using list comprehension.
# Output: 166

count = 0
for i in range(1, 1000 + 1):
    if i % 6 == 0:
        count += 1

print(count)