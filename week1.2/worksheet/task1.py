# Worksheet 1.2: Task 1 Solution

import sys

grade = input("Please enter your grade: ")

if not grade.isnumeric():
    sys.exit("Error: Grade must be an integer between 0 and 100)
else:
    grade = int(grade)

    if grade < 0 or grade > 100:
        sys.exit("Error: Grade must be an integer between 0 and 100)

if grade >= 0 and grade <= 39:
    print(f"{grade} is a Fail")
elif grade >= 40 and grade <= 69:
    print(f"{grade} is a Pass")
else:
    print(f"{grade} is a Distinction")