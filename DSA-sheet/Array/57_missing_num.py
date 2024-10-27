arr = [4, 3, 1, 0, 2, 5, 6, 7, 9]
# for i in range(0, len(arr) + 1):
#     if i not in arr:
#         print(i)


n = len(arr)
#
# dict = {}
#
# for i in range(0, n):
#     dict[i] = 0
#
# for i in range(0, n):
#     dict[arr[i]] = 1
# for k, v in dict.items():
#     if v == 0:
#         print(k)
original_total = (n * (n + 1)) // 2
print(original_total - sum(arr))
