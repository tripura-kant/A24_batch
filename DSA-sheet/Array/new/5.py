# Right Rotate an array by one place

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
n= len(nums)

nums[:] = nums[-1] + n[0: n-1]
print(nums)
