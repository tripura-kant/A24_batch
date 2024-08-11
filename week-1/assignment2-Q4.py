# Write a Python program that takes a student's score as input and
# prints the corresponding grade. Use the following grading scale:
# A: 90-100
# B: 80-89
# C: 70-79


def grading(score):
    if 90 <= score <= 100:
        print("A")
    elif 80 <= score < 90:
        print("B")
    elif 70 <= score < 80:
        print("C")
    elif 60 <= score < 70:
        print("D")
    else:
        print("F")


score = int(input("Enter score "))
grading(score)
