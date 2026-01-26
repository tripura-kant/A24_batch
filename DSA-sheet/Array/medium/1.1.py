# tWO SUM PROBLEM

nums = [5,9,1,2,4]
target = 13
n = len(nums)
hashmap = {}

for i in range(0, n):
    remaining = target - nums[i]
    if remaining in hashmap:
        print(hashmap[remaining], i)
    hashmap[nums[i]] = i
    
        