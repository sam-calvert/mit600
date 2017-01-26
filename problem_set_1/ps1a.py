#!/bin/python3

"""
Paying the Minimum
Problem 1
Write a program to calculate the credit card balance after one year if a person only pays the
minimum monthly payment required by the credit card company each month.
Use raw_input() to ask for the following three floating point numbers:
    1. the outstanding balance on the credit card
    2. annual interest rate
    3. minimum monthly payment rate
For each month, print the minimum monthly payment, remaining balance, principle paid in the
format shown in the test cases below. All numbers should be rounded to the nearest penny.
Finally, print the result, which should include the total amount paid that year and the remaining
balance.
"""

# Get user input for variable values

balance = float(input("Enter the outstanding balance on your credit card: "))
interest_rate = float(input("Enter the anual credit card interest rate as a decimal: "))
pay_rate = float(input("Enter the minimum monthly payment rate as a decimal: "))
total_paid = 0

# Calculate minimum monthly payment, remaining baloance, and principal paid for each month in the year

for month in range(1,13):
    interest = interest_rate/12 * balance
    payment = pay_rate * balance
    total_paid += payment
    balance -= payment - interest
    print("Month: %d \n Minimum monthly payment: $%.2f \n\
            Principal paid: $%.2f \n Remaining balance: $%.2f"\
            % (month, payment, payment - interest, balance))

print("Total amount paid: %.2f \n Remaining balance: %.2f" \
        % (total_paid, balance))
