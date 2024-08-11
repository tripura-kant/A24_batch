def pattern(n: int):
    for i in range(1, n + 1):
        for j in range(n, 0, -1):
            print(j, end=" ")
        print()


n = 5
pattern(n)
