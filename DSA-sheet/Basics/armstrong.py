def check_arm(n):
    num = n
    nod = len(str(num))
    total = 0

    while num > 0:
        ld = num % 10
        total = total + (ld ** nod)
        num = num // 10

    return n == total


n = 153
print(check_arm(n))
