def func(nums):
    n = len(nums)

    if n == 1:
        return

    # Pointer for the position to place the next non-zero element
    i = 0

    # Move all non-zero elements to the front
    for j in range(n):
        if nums[j] != 0:
            nums[i] = nums[j]
            i += 1

    # Fill the remaining part of the array with zeros
    while i < n:
        nums[i] = 0
        i += 1

    print(nums)


# Test the function
nums = [0, 1, 0, 3, 12, 0]
func(nums)
