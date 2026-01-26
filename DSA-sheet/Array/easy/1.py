#  Largest element in an array

nums = [23,2,-97,99,67]

result = float("-inf")

for num in nums:
    if result < num:
        result = num

print(result)

