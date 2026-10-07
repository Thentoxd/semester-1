"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Alex Nicklin
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
amount = input("Enter your monthly savings amount: ")

if not amount.isnumeric():
    print("Invalid amount")
    exit()

amount = int(amount)

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.

yearly_total = amount * 12
print(f"You will save £{yearly_total} every year.")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).
yearly_interest_total = yearly_total * 1.008
print(f"With interest, you will save £{yearly_interest_total:.2f} per year.")

