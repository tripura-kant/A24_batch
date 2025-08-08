#Write a function that removes all vowels (a, e, i, o, u) from a given
# string?=

def remove_vowels(s):
    result = ""
    for char in s:
        if char not in "aeiou":
            result += char

    return result

s = "adfsdfsdferw"
print(remove_vowels(s))