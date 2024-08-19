def reverse(num):
    n = num
    result = 0
    while n > 0:
        ld = n % 10
        result = (result * 10) + ld
        n = n // 10
    return result


num = 1257
print(reverse(num))
