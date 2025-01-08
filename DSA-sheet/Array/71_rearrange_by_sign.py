nums = [3, -2, 1, -5, 2, -4]

pos = []
neg = []
n = len(nums)

for i in range(len(nums)):
    if nums[i] > 0:
        pos.append(nums[i])
    else:
        neg.append(nums[i])

print(pos)
print(neg)

for i in range(len(pos)):
    nums[2 * i] = pos[i]
    nums[2 * i + 1] = neg[i]

print(nums)
