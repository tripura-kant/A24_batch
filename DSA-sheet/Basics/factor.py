num = 4
result = []

# # Brute force
# for i in range(1, num + 1):
#     if num % i == 0:
#         result.append(i)
#
# print(result)

# Optimal
# for i in range(1, num // 2):
#     if num % i == 0:
#         result.append(i)
#
# result.append(num)
#
# print(result)
from math import sqrt

result = []
for i in range(1, int(sqrt(num)) + 1):
    if num % i == 0:
        result.append(i)
        if num // i != i:
            result.append(num // i)

result.sort()
print(result)

result.append(num)
