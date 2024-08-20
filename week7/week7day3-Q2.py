# Armstrong Nuumber 11

def check_Arm(num):
    n = num
    nod = len(str(n))
    result = 0

    while n > 0:
        ld = n % 10
        result = result + (ld ** nod)
        n = n // 10
    return result == num


num = 153
print(check_Arm(num))
