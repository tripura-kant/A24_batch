# Write a function that takes a string and returns it in uppercase.

def uppercase(s):
    uppercase_string = ""
    for char in s:
        if "a" <= char <= "z":
            uppercase_string += chr(ord(char) - 32)
        else:
            uppercase_string += char
    return uppercase_string


my_string = "aB677^&*hx"

print(uppercase(my_string))            