nums = [1, 2, 3, 4, 5, 6, 19, 8, 9, 10]

n = len(nums)
for i in range(n-1):
    if nums[i] > nums[i+1]:
        print("false")
        break
else:
    print("True")