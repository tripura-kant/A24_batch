# reverse array

n = [1,2,5,6,9,2]
def reverse_array(n):
    left = 0
    right = len(n)-1
    while left < right:
        n[left], n[right] = n[right], n[left]
        left += 1
        right -= 1
    return n

result = reverse_array(n)
print(result)

