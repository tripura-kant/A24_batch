# Write a python program to interchange first and last elements in a list.

from typing import List
def interchange(my_list):
    my_list[0], my_list[-1] = my_list[-1], my_list[0]
my_list = ["Anirudh", 6, 4, 110.654, True, -54]
interchange(my_list)
print(my_list)