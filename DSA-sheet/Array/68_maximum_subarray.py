# nums = [-2, 1, 2, 0, -3, -5, 4]
# maxi = float('-inf')
# n = len(nums)
# for i in range(0, n):
#     total = 0
#     for j in range(i, n):
#         total += nums[j]
#         maxi = max(maxi, total)
#
# print(maxi)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

maxi = float('-inf')
n = len(nums)

for i in range(n):
    for j in range(i, n):
        total = 0
        for k in range(i, j + 1):
            total += nums[k]  # Add the current number to the subarray sum
        maxi = max(maxi, total)  # Update the maximum sum if needed

print(maxi)
