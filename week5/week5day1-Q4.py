# Write a function that counts the number of words in a given string.
# (String may only contain alphabets and spaces


my_string = "python is easy to learn"


def count_words(my_string):
    count = 0
    result = my_string.split()
    for word in result:
        count += 1  
    return count
print(count_words(my_string))        







# def count_words(s):
#     return len(s.strip().split())

# s = "Hello world is Python"
# print(count_words(s))


