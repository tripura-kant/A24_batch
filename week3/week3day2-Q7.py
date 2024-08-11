def pattern(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


n = 5
pattern(n)
