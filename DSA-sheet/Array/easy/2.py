#Find the second largest element in an array


nums = [23,2,-97,99,67, 88]

largest = float("-inf")

sec_largest = float("-inf")

for num in nums:
    if num > largest:
        largest = num

for num in nums:
    if num < largest and num > sec_largest:
        sec_largest = num        

print(largest)
print(sec_largest)