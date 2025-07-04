# Use a do-while loop to print a countdown from 10 to 1.

num = 10
while True:
    print(num, end=" ")
    num -= 1

    if num == 0:
        break