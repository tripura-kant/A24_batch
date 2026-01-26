nums2 = [1, 2, 3, 4, 5, 7, 8, 9, 0]    

n = len(nums2)

freq = {}

for i in range(0, n+1):
    freq[i] = 0

for num in nums2:
    freq[num] = 1

for k, v in freq.items():
    if v == 0:
        print(k)

# print(freq)