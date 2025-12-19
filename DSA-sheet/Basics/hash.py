n = [1,2,4,6,7]
m = [10,2,3,1,6]

for num in m:
    count = 0
    for x in n:
        if x == num:
            count += 1

    print(count)        