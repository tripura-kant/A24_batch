my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = {}
for key in my_list:
    result[key] = result.get(key, 0 ) + 1

# print(result)    
