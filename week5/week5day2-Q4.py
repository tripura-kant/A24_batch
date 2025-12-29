# Write a function that takes a dictionary and a key, and returns True if
# the key is found in the dictionary, otherwise False.

def does_key_exists(d, key):
    return key in d

d = {"anirudh": 45, 56: 78, "gender": "Male", 11: 22}
print(does_key_exists(d, "xyz"))