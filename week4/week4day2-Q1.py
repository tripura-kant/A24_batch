# Take 10 integer inputs from user and store them in a list. Now, copy all
# the elements in another list but in reverse order.

list = []
start=int(input("Enter Start    "))
end=int(input("Enter End    "))
for i in range(start, end+1):
    list.append(i)
print(list)
list.reverse()
print(list)