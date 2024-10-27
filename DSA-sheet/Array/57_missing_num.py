arr = [4, 3, 1, 0]
# for i in range(0, len(arr) + 1):
#     if i not in arr:
#         print(i)


n = len(arr)

dict = {}

for i in range(0, n):
    dict[i] = 0

for i in range(0, n):
    dict[arr[i]] = 1
for k, v in dict.items():
    if v == 0:
        print(k)
