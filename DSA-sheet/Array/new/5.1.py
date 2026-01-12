# Right Rotate an array by one place

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

n = len(nums)
temp = nums[n-1]
# print(temp)

for i in range(n-2, -1, -1):
    nums[i+1] = nums[i]
nums[0] = temp

print(nums)