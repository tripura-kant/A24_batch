#Find missing number

nums = [9,6,5,4,3,2,1,4,7,10,0]

for i in range(len(nums)):
    if i not in nums:
        print(i)

