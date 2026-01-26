# Remove Duplicates from a Sorted Array

#phle dictionary freq map banao fir j zeo leke nums ko change kro aur j ka count    
# nums = [23,24,499,2]

nums = [23,23,24,499, 560,999, 23, 24]

n = len(nums)

if len(nums) == 1:
    print(1)
i = 0
j = i + 1
while j < len(nums):
    if nums[j] != nums[i]:
        i += 1
        nums[j], nums[i] = nums[i], nums[j]
    j += 1
print(i + 1)