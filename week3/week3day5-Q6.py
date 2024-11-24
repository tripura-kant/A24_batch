# my_list = [4, 8, 6, 5, 3, 12, 1, 7, 6, 20, 15, 25]
# new_list = []
# n = len(my_list)
# for num in range(n - 1, -1, -1):
#     if my_list[num] % 5 == 0:
#         new_list.append(my_list[num])
# print(new_list)

my_list = [4, 8, 6, 5, 3, 12, 1, 7, 6, 20, 15, 25]
n = len(my_list)
for i in range(n - 1, -1, -1):
    if my_list[i] % 5 == 0:
        print(my_list[i], end=" ")
