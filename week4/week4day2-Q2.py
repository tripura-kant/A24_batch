# Make a list. Write a simple program for addition of the 2nd element
# from start and 2nd element from the end.

list = []
l = int(input("Enter list length "))
for i in range(l):
    num = int(input("Enter number {} ".format(i+1)))
    list.append(num)

print(list)

sum = list[1] + list[-2]
print(sum)