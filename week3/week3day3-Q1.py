n = 5

for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()

# n = int(input("Enter number of lines = "))
# for i in range(1, n + 1):
#     for j in range(1, n - i + 1):
#         print(" ", end=" ")
#     for k in range(1, i + 1):
#         print(k, end=" ")
#     print()
