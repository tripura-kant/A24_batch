def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    small = float("inf")
    second_small = float("inf")
    large = float("-inf")
    second_large = float("-inf")

    for i in range(0, len(a)):
        small = min(small, a[i])
        large = max(large, a[i])

    for i in range(0, len(a)):
        if a[i] < second_small and a[i] != small:      # candidate > min
            second_small = a[i]
        if a[i] > second_large and a[i] != large:      # candidate < max
            second_large = a[i]

    return [second_large, second_small]


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(getSecondOrderElements(len(a), a))