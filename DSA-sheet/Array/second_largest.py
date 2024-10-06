#

arr = [5, -10, 13, 67, 89, -100, 55]


def find_second_max(arr):
    maxi = float('-inf')
    mini = float('inf')
    n = len(arr)
    sec_max = float('-inf')
    sec_mini = float('inf')
    for i in range(0, n):
        if arr[i] > maxi:
            sec_max = maxi
            maxi = arr[i]

        elif arr[i] > sec_max and arr[i] != maxi:
            maxi = arr[i]

        elif arr[i] < mini:
            sec_mini = mini
            mini = arr[i]

        elif arr[i] < sec_mini and arr[i] != mini:
            sec_mini = arr[i]

    return maxi, mini, sec_mini, sec_max


print(find_second_max(arr))
