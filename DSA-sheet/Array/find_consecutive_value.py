nums = [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1]

max_cnt = 0

cnt = 0
for i in range(0, len(nums)):
    if nums[i] == 1:
        cnt += 1
    else:
        max_cnt = max(max_cnt, cnt)
        cnt = 0
print(max(max_cnt, cnt))
