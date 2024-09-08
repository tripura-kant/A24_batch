def check_pal(n):
    num = n
    result = 0

    while num > 0:
        ld = num % 10
        result = (result * 10) + ld
        num = num // 10

    return n == result


n = 1212
print(check_pal(n))
