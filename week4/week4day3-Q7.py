# Ask an integer n from the user. Write a Python program to generate a
# list of powers of 2 from 1 to n using List Comprehension
# Example input: n = 6
# Example output: [1, 4, 9, 16, 25, 36]

def powerofN(n):
    for i in range(1, n + 1):
        i = i ** 2
        print(i, end=" ")

n = 6
powerofN(n)
