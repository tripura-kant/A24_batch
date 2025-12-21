# Ask 10 numbers from the user and put them into the list. Now remove
# all the even numbers from that list.

def user_num():
    user_list = []
    results = []
    for i in range(10):
        num = int(input(f"(number {i})"))
        user_list.append(num)
    
    for i in user_list:
        if i % 2 != 0:
               results.append(i)
    return results           

result = user_num()
print(result)    