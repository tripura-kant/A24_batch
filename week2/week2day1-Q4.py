num1 = int(input())
num2 = int(input())
operation = input()


def simple_calculator(num1, num2, operation):
    if operation == "+":
        answer = num1 + num2
    else:
        answer = num1 - num2

    print(f"{answer}")


simple_calculator(num1, num2, operation)
