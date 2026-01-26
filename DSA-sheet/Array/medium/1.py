# Two sum problems

nums = [1,2,6,9,8,7,6,5,4,2]

n = len(nums)
target = 13

for i in range(0, n-1):
    for j in range(i+1, n):
        if nums[i] + nums[j] == target:
            print(i,j)

