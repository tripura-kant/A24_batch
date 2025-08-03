# 3. Ask 10 numbers from the user and put them into the list. Now remove
# all the even numbers from that list.

my_list=[]
l = int(input("Enter list length    "))

for i in range(l):
    num = int(input(f"Enter number {i+1} "))
    if num % 2 != 0:
        my_list.append(num)

print(my_list)


