import math


def count_digits(num: int) -> int:
    return math.floor(math.log10(num) + 1)


print(count_digits(1234))
