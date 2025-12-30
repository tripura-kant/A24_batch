import os

for i in range(1, 12):
    filename = f"week6day1-Q{i}.py"
    os.open(filename, os.O_CREAT | os.O_APPEND)
