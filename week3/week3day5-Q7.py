my_list = [5, -8, 10, -15, 2, -4, 95, -34, 25]

n = len(my_list)
maxi = -float('inf')
for num in range(0, n):
    if my_list[num] > maxi:
        maxi = my_list[num]

print(maxi)
