my_list = [4, 8, 6, 5, 3, 12, 1, 3]

count = 0

for i in my_list:
    if i % 2 != 0:
        count += 1

print(f"Total odd numbers = {count}")
