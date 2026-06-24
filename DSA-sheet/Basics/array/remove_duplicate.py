nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1,2,3,4,5,6,7,8,9,10,11]

n = len(nums)
freq_map = {}
for i in range(n):
    freq_map[nums[i]] = 0

j = 0
for k in freq_map:
    nums[j] = k
    j = j + 1
print(j)