# Selection Sort


nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
def selection(nums):
    n = len(nums)
    
    for i in range(0, n):
        min_index = i
        for j in range(i+1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]


    return nums

result = selection(nums)
print(result)            
