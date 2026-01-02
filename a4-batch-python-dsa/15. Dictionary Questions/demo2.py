my_list = "aassdasdkdjhakjdiuqwyhbkakcxnbghdffffffffffaaaaaaaaaa"

max_freq = 0
max_elem = 0

result = {}

for i in my_list:
    result[i] = result.get(i, 0) + 1

for elem in result:
    if result[elem] > max_freq:
        max_freq = result[elem] 
        max_elem = elem

print(max_freq)
print(max_elem)