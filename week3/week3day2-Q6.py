def pattern(n):
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            print(j, end=" ")
        print()


n = 5
pattern(n)
