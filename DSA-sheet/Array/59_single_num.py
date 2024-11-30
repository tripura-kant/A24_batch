nums = [4, 1, 2, 1, 2]

# freq = {}
# for num in nums:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1
# for num in freq:
#     if freq[num] == 1:
#         print(num)
n = len(nums)
for i in range(0, n):
    count = 0
    for j in range(0, n):
        if nums[j] == nums[i]:
            count += 1

    if count == 1:
        print(nums[i])
