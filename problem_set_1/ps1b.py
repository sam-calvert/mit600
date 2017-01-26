#!/bin/python3

"""
Paying Debt Off In a Year
Problem 2
Now write a program that calculates the minimum fixed monthly payment needed in order pay
off a credit card balance within 12 months. We will not be dealing with a minimum monthly
payment rate.
Take as raw_input() the following floating point numbers:
    1.       the outstanding balance on the credit card
    2.       annual interest rate as a decimal
Print out the fixed minimum monthly payment, number of months (at most 12 and possibly less
than 12) it takes to pay off the debt, and the balance (likely to be a negative number).
Assume that the interest is compounded monthly according to the balance at the start of the
month (before the payment for that month is made). The monthly payment must be a multiple of
$10 and is the same for all months. Notice that it is possible for the balance to become negative
using this payment scheme. In short:
    Monthly interest rate = Annual interest rate / 12.0
    Updated balance each month = Previous balance * (1 + Monthly interest rate) – Minimum
    monthly payment
"""

# Gather user input

balance = float(input("Enter the outstanding balance on your credit card: "))
interest_rate = float(input("Enter the anual credit card interest rate as a decimal: "))

# Set payment to $10 and test whether this will pay off the balance
# Increase payment by $10 until the correct answer is found
set_balance = balance
payment = 10
while True: 
    balance = set_balance
    for month in range(1,13):
        balance *= interest_rate/12 + 1
        balance -= payment
        if balance <= 0:
            break
    if balance <= 0:
        break
    payment += 10
print("RESULT \nMonthly payment to pay off debt in 1 year: %d \
        \nNumber of months needed: %d \nBalance: %.2f" \
        % (payment, month, balance))
