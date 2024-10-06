def getSecondOrderElements(n: int, a: [int]) -> [int]:
    maxi = float('-inf')
    sec_max = float('-inf')
    mini = float('inf')
    sec_mini = float('inf')

    for i in range(n):
        # Update maximum and second maximum
        if a[i] > maxi:
            sec_max = maxi
            maxi = a[i]
        elif a[i] > sec_max and a[i] != maxi:
            sec_max = a[i]

        # Update minimum and second minimum
        if a[i] < mini:
            sec_mini = mini
            mini = a[i]
        elif a[i] < sec_mini and a[i] != mini:
            sec_mini = a[i]

    # Return None for sec_max or sec_mini if they do not exist
    return (sec_max if sec_max != float('-inf') else None,
            sec_mini if sec_mini != float('inf') else None)
