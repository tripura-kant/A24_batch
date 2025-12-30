# Given a dictionary, write a function that returns a new dictionary
# containing only the keys that have values of type str.
# Input:
# Output:

my_dict = {"a": "b", "z": 12, "adult": True, "gender": "Male"}

result = {}

for i in my_dict:
    if isinstance(my_dict[i], str):
        result[i] = my_dict[i]

print(result)