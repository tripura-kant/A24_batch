# Make a list of your own. Make two more empty list like odd and even.
# Put all the even numbers from original list to even and odd numbers to
# odd and print both lists. (Don’t remove anything from original one)


original = [1,2,3,3,42,2,12,4,4,4,5,7,8,8,9,9,909,0,6,655,5,5,4,43,34,3]

odd = []
even = []

n = len(original)
for i in range(n):
    if original[i] % 2 == 0:
        even.append(original[i])
    else:
        odd.append(original[i])

print(f"odd list is {odd}")
print(f"even list is {even}")