# Input: "apple mango apple orange"
# Output: apple -> 2  
#               mango -> 1  
#               orange -> 1

words_list = "apple mango apple orange"
count_freq = {}

# for word in words_list.split():
#     count_freq[word] = count_freq.get(word, 0) + 1

# print(count_freq)

for word in words_list.split():
    count_freq[word] = count_freq.get(word, 0) + 1
print(count_freq)