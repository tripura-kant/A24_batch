#  Write a function that counts the number of words in a given string.
# (String may only contain alphabets and spaces)

def count_words(s):
    return len(s.strip().split())

s = "Hello world is Python"
print(count_words(s))


