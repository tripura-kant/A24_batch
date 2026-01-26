# Remove Duplicates from a Sorted Array

#phle dictionary freq map banao fir j zeo leke nums ko change kro aur j ka count    
# nums = [23,24,499,2]

nums = [23,23,24,499, 560,999, 23, 24]

n = len(nums)
freq_map={}
for num in nums:
    freq_map[num] = freq_map.get(num, 0) + 1 
print(freq_map)

j = 0
for k in freq_map:
    nums[j] = k
    j += 1

print(j)

print(nums)