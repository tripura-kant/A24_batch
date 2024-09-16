def sorted_and_ordered(arr):
    dict = {}

    if len(arr) == 1:
        return 1

    i = 0
    j = i + 1

    while j < len(arr):
        if arr[i] != arr[j]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

        j += 1
    return i + 1


arr = [0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5]
print(sorted_and_ordered(arr))
