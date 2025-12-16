# Dictionary
nums = [2,3,3,4,1,1,2,7,8,9,2,1,3,4,4,6,7,0]
freq_map = {}

for i in range(0, len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1

print(freq_map[7])
