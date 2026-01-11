# Check if the array is sorted

# nums = [23,2,-97,99,67, 88]

nums = [23,24,499]

is_sorted = True
n = len(nums)

for i in range(0, n-1):
    if nums[i] > nums[i+1]:
        is_sorted = False
        break

print(is_sorted)    