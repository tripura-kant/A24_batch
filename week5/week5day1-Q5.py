# Write a function that finds and returns the longest word in a given
# string
def longest_word(s):
    longest = ""
    for word in s.split():
        if len(word) > len(longest):
            longest = word
    return longest        

my_string = "python is a very easy coding language to learnhgfhgfhfhg"
print(longest_word(my_string))