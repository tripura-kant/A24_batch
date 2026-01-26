# Implementing Linear Search

nums = [1, 2, 3, 4, 5, 0, 6, 7, 0, 0]

target = 4

n = len(nums)

for i in range(0, n):
    if nums[i] == 4:
        print(i)