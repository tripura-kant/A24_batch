nums = [1, 2, 1, 2, 0, 1, 1, 1, 1, 0, 0]

n = len(nums)
zero = 0
one = 0
two = 0

for i in range(0, n):
    if nums[i] == 0:
        zero += 1
    elif nums[i] == 1:
        one += 1
    else:
        two += 1

for i in range(0, zero):
    nums[i] = 0

for i in range(zero, zero + one):
    nums[i] = 1

for i in range(zero + one, n):
    nums[i] = 2

print(nums)
