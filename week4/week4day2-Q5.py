lst = [33, 11, 22, 22]

def removeNth(lst, n):
    i = 0
    while i < len(lst):
        if lst[i] == n:
            lst.pop(i)  # remove element at index i
        else:
            i += 1
    print(lst)

removeNth(lst, 2)
print(lst)