# Make two lists of same length and pass it to a function.
# Return a third list where each element is the sum of index

def sumofindex(list1, list2):
    sum = []
    l = len(list1)
    for i in range(l):
        sum.append(list1[i] + list2[i])

    print(sum)

sumofindex(list1=[1,3,4,7], list2=[2,3,4,5])