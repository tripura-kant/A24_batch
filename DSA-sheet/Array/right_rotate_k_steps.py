nums = [1, 1, 4, 9, 4, 7, 1]
n = len(nums)
k = 9
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
