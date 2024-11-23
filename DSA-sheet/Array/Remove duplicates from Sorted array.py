arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

if len(arr) == 1:
    print(1)
i = 0
j = i + 1

while j < len(arr):
    if arr[i] != arr[j]:
        i += 1
        arr[i], arr[j] = arr[j], arr[i]
    j += 1
print(i + 1)
# n = len(arr)
# dict = {}
# for i in range(0, n):
#     dict[arr[i]] = 0
# print(arr)
# print(dict)
# j = 0
# for key in dict:
#     arr[j] = key
#     j += 1
#
# print(j)
