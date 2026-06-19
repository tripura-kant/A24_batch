#5873
n = 5873445


num = n
i = 0
while num > 0:
    last_digit = num%10
    # print(last_digit, end="")
    num=num//10
    i += 1
print(i)    