#  Ask a string from user. Store the frequency of each character in the
# dictionary. Then print the character with the maximum frequency.


my_input = input("Enter the string  ")

res = {}

for i in my_input:
    res[i] = res.get(i, 0) + 1

print(res)

max_char, max_freq = max(res.items(), key = lambda item:item[1])
print(max_char, max_freq)