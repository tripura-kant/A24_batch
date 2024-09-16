# Check if array is sorted and rotated

arr = [2, 4, 9, 11, 14, 16]


def check_sorted_rotated(arr):
    n = len(arr)
    rotation = 0
    for i in range(0, n - 1):
        if arr[i] > arr[(i + 1) % n]:
            rotation += 1
        if rotation > 1:
            return False
    return True


print(check_sorted_rotated(arr))
