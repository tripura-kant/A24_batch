# Make your own list of numbers. Ask a start and end position from User.
# Print the list from start position to end position using Slicing.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start=int(input("Enter start "))
end=int(input("Enter end "))

result = []
for i in range(start, end+1):
    result.append(my_list[i])

print(result)

