nums = [5, 6, 1, 2]
k = 3
for _ in range(k):
    elem = nums.pop()
    nums.insert(0, elem)

print(nums)
