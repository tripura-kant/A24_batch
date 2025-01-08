arr = [2, 4, 6, 7, 10]
target = 7
n = len(arr)
low = 0
high = n - 1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        print(mid)
        break
    elif target < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1
else:
    print("Not present -1")
