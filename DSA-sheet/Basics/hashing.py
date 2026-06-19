n = [5,3,1,2,6,7,9,10]
m = [23,4,5,21,1,10,9]

result = {}
for i in n:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
# print(result)

output = {}
for value in m:
    if value in result:
        output[value] = result[value]

print(output)
        
