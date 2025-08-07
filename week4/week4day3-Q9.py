# Ask an integer n from user. Create a list which contains all the prime
# numbers from 1 to n using list comprehension.
# Input: n = 20
# Output: [2, 3, 5, 7, 11, 13, 17, 19]

def is_prime_number(num: int) -> bool:
    # I have not used factors logic here
    # I will be explaning this in next lecture
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


n = int(input("Enter n = "))
my_list = [i for i in range(2, n + 1) if is_prime_number(i)]
print(my_list)