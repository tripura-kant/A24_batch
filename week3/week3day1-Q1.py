def pattern(n: int):
    for i in range(1, n + 1):
        for j in range(1, 6):
            print(1, end=" ")
        print()


n = 5
pattern(n)
