# Check if the number entered by User is divisible by 3 or not.


def check_divisibility(num):
    if num % 3 == 0:
        print("Divisible by 3")
    else:
        print("Not Divisible by 3")


num = int(input("enter num "))
check_divisibility(num)
