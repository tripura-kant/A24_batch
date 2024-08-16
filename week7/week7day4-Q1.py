# Count Digits | Practice | GeeksforGeeks
# Extraction of digits
###

num = 567819
n = num
while n > 0:
    ld = n % 10
    print(n)
    n = n // 10
