# Move zero at end

nums = [1,0,2,4,3,2,0,2,0]
temp = []
n = len(nums)
for i in range(len(nums)):
    if nums[i] != 0:
        temp.append(nums[i])
print(temp)
nz = len(temp)
for i in range(nz):
    nums[i] = temp[i]
for i in range(nz, n):
    nums[i] = 0
print(nums)

