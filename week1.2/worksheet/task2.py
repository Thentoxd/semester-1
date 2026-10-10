# Worksheet 1.2: Task 2 Solution

import sys
from util import read_numbers

numbers = read_numbers()
numbers.sort()

size = len(numbers)

if size == 0:
    sys.exit("Error: no numbers provided")
else:
    median = 0
    # Note: Line 7 already sorts the list
    if size % 2 == 0:
        # If the size of the list is even, print out the average of the two middle values.
        median = (numbers[size // 2] + numbers[(size // 2) - 1]) / 2
    else:
        #Otherwise, just print out the middle value.
        median = numbers[size // 2]

    print(f"Minimum = {min(numbers)}")
    print(f"Maximum = {max(numbers)}")
    print(f"Mean = {sum(numbers) / size}")
    print(f"Median = {median}")