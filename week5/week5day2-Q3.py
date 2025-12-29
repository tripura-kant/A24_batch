# Create two list. One would be subject name and other would be marks.
# Join both the list to make it as a dictionary. (The length of two lists should
# be the same).

subject = ["history", "maths", "science", "eng"]
marks = [45, 63, 22, 11]
result = {}
def create_dict(subject, marks):
    for value in range(len(marks)):
            result[subject[value]] = marks[value]
    return result

ans = create_dict(subject, marks)
print(ans)


