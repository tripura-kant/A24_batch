#Write a function that removes all vowels (a, e, i, o, u) from a given
# string?=

# def remove_vowels(s):
#     result = ""
#     for char in s:
#         if char not in "aeiou":
#             result += char

#     return result

# s = "adfsdfsdferw"
# print(remove_vowels(s))


def remove_vowels(s: str) -> str:
    vowels = "aeiouAEIOU"
    no_vowels = ""
    for char in s:
        if char not in vowels:
            no_vowels += char
    return no_vowels


my_string = "abcdefghij"
print(remove_vowels(my_string))