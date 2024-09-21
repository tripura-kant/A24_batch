# Maximum Consecutive Ones

arr = [0, 0, 0, 1, 1, 0, 1, 1, 1, 1]


def max_one(arr):
    max_count = 0
    count = 0

    for i in range(0, len(arr)):
        if arr[i] == 1:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0

    return max(max_count, count)


print(max_one(arr))
