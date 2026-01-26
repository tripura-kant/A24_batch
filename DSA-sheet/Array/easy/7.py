# Move Zeroes 

nums = [1, 2, 3, 4, 5, 0, 6, 7, 0, 0]
n = len(nums)
temp = []

for i in range(0, n):
    if nums[i] != 0:
        temp.append(nums[i])

nz = len(temp)
for i in range(0, nz):
    nums[i] = temp[i]

for i in range(nz, n):
    nums[i] = 0

print(nums)