# Write a program to check if number is divisible by 2 and 3 but not 8.

def num_check(num):
    if num % 2 == 0 and num % 3 == 0 and num % 8 != 0:
        print("divisible")
    else:
        print("not divisible")


num = int(input("Enter no "))
num_check(num)
