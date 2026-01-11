#  Largest element in an array

nums = [23,2,-97,99,67]

result = nums[0]
n = len(nums)
for num in range(0,n):
    if result < num:
        result = num

print(result)

