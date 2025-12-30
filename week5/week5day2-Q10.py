# Write a Python program to combine two dictionary by adding values
# for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}

res = {}

for i in d1:
    res[i] = d1[i]
print(res)

for i in d2:
    res[i] = res.get(i, 0) + d2[i]

print(res)