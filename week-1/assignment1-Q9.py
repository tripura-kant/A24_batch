# Take values of length and breadth of a rectangle from user and check if
# it is square or not.

def rectangle(length, breadth):
    if length == breadth:
        print("square")
    else:
        print("not square")


length = int(input("enter num "))
breadth = int(input("enter num "))
rectangle(length, breadth)
