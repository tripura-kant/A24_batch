# Q2. A student will not be allowed to sit in exam if his/her attendance is less
# than 75%. Take following input from user
# Number of classes held
# Number of classes attended.
# 1. Print percentage of class attended
# 2. Print Is student is allowed to sit in exam or not

def attendance_check(total_class, class_attend):
    attendance_percent = (class_attend / total_class) * 100
    print(attendance_percent)
    if attendance_percent >= 75:
        print("allowed")
    else:
        print("not allowed")


total_class = int(input("Enter num "))
class_attend = int(input("Enter num "))
attendance_check(total_class, class_attend)
