# Q1. Write a program that takes two numbers as input and checks if the first
# number is divisible by the second.


def check_divisibility(num1, num2):
    if num1 % num2 == 0:
        print("divisible")
    else:
        print("not divisible")


num1 = int(input("enter num "))
num2 = int(input("enter num "))
check_divisibility(num1, num2)
