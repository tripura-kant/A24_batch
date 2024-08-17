# Count Digits | Practice | GeeksforGeeks
# Extraction of digits
###

num = 567811

count = 0
n = num
while n > 0:
    count += 1
    n = n // 10
print(count)
