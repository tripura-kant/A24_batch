# Make a list. Write a simple program for addition of the 2nd element
# from start and 2nd element from the end

def addition(list):
    num1 = list[1]
    num2 = list[-2]
    result = num1 + num2
    return result

list = [1,2,3,4,3,22,2]
print(addition(list))



# # Write a function that takes a string and returns it in uppercase.

# def uppercase(s):
#     uppercase_string = ""
#     for char in s:
#         if "a" <= char <= "z":
#             uppercase_string += chr(ord(char) - 32)
#         else:
#             uppercase_string += char
#     return uppercase_string


# my_string = "aB677^&*hx"

# print(uppercase(my_string))            