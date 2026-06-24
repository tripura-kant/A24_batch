# Right Rotate an Array by K places

# Right Rotate an Array by K places
k =3
nums = [5,2,21,1,1,1,1]

n = len(nums)
rotation = k % n
for i  in range(0, rotation):
    e = nums.pop()
    nums.insert(0, e)
print(nums)