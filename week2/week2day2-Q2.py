def check_even_odd(num):
    if num % 2 == 0:
        return True
    else:
        return False


num = int(input())

x = check_even_odd(num)
print(x)
