# Write a program using nested loops to print a multiplication table
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end="")  # 4 spaces width per number
    print()
