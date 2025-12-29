# Q2. Given a list of integers, create a dictionary that stores each unique
# integer as a key and its frequency as the value. Find the integer with the
# maximum frequency.
# Example Input: [4, 5, 6, 5, 4, 4, 7]
# Expected Output: 4 (Frequency: 3


my_list = [4, 5, 6, 5, 4, 4, 7]
result = {}

for elem in my_list:
        result[elem] = result.get(elem, 0) + 1

print(result)    

max_elem = max(result, key=result.get)
print(max_elem)
print(f"{max_elem} (Frequency: {result[max_elem]})")