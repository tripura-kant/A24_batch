def arm(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10

    return count

n = 320
print(arm(n))
