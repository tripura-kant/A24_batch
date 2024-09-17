nums = [5, 6, 1, 2, 2]
n = len(nums)
k = 3
# for _ in range(k):
#     elem = nums.pop()
#     nums.insert(0, elem)
#
# print(nums)
rotatation = k % n
for _ in range(rotatation):
    elem = nums.pop()
    nums.insert(0, elem)

print(nums)
