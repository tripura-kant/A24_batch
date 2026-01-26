# Rotate k times

nums = [1, 2, 3, 4, 5, 6, 7]

n = len(nums)
k = 3
rotation = k % n

for _ in range(0, rotation):
    e = nums.pop()
    nums.insert(0, e)

print(nums)