#  Given two dictionaries, write a function to merge them into a new
# dictionary. If there is any overlap of keys, the value from the second
# dictionary should overwrite the one from the first dictionary.
# Dictionary 1:
# {'apple': 3, 'banana': 5, 'cherry': 7}
# Dictionary 2:
# {'banana': 8, 'orange': 10, 'apple': 9}
# Expected Output:
# {'apple': 9, 'banana': 8, 'cherry': 7, 'orange': 10}

dict1 = {'apple': 3, 'banana': 5, 'cherry': 7}
dict2 = {'banana': 8, 'orange': 10, 'apple': 9}
result = {}

for i in dict1:
    result[i] = dict1[i]

for i in dict2:
    result[i] = dict2[i]
    

print(result)