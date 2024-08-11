# . Ask a number from user. Print if the number is ODD or EVEN.


def check_odd_even(num):
    if num % 2 == 0:
        print("EVEN")
    else:
        print("ODD")


num = int(input("enter num "))
check_odd_even(num)
