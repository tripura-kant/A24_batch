# Ask number of subjects from the user. Ask the subject name and marks
# from the user and store that into the dictionary and print it.

result = {}

no_of_sub = int(input("Enter number of subject  "))


for i in range(no_of_sub):
    sub_name = input("Enter number of subject   ")
    marks = int(input("Enter number of subject  "))
    result[sub_name] = marks

print(result)