my_list = [4, 8, 6, 5, 3, 12, 1, 3, 6]

n = len(my_list)
odd = 0
even = 0

for i in range(n):
    if my_list[i] % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Total even numbers = {even}")
print(f"Total odd numbers = {odd}")
