nums = [0, 1, 0, 3, 12, 0]
non_zero_list = []
n = len(nums)
for i in range(0, n):
    if nums[i] != 0:
        non_zero_list.append(nums[i])

# print(non_zero_list)
n_z_l = len(non_zero_list)

for i in range(0, n_z_l):
    nums[i] = non_zero_list[i]
for i in range(n_z_l, n):
    nums[i] = 0
print(nums)
