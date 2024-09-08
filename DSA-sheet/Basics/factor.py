num = 17
result = []

# Brute force
for i in range(1, num + 1):
    if num % i == 0:
        result.append(i)

print(result)

# Optimal
# for i in range(1, num // 2):
#     if num % i == 0:
#         result.append(i)
#
# result.append(num)
#
# print(result)
