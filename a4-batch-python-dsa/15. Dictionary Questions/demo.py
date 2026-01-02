my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,9,9]

result = {}
max_freq = 0
max_elem = 0

for key in my_list:
    result[key] = result.get(key, 0 ) + 1

# print(result)    
for elem in result:
    if result[key] > max_freq:
        max_freq = result[key]
        max_elem = elem

print(max_freq)
print(max_elem)
