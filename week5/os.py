import os

for i in range(1, 12):
    filename = f"week5day2-Q{i}.py"
    os.open(filename, os.O_CREAT | os.O_APPEND)
