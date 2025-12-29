# Input: "apple mango apple orange"
# Output: apple -> 2  
#               mango -> 1  
#               orange -> 1

words_list = "apple mango apple orange"
count_freq = {}


for word in words_list.split():
    if word in words_list.split():
        print(word)
        count_freq[word] = count_freq[word] + 1
    else:
        count_freq[word] = 1

    print(count_freq)