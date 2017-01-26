#!/bin/python3

"""
Monthly payment lower bound = Balance / 12.0
Monthly payment upper bound = (Balance * (1 + (Annual interest rate / 12.0)) ** 12.0) / 12.0

Problem 3
Write a program that uses these bounds and bisection search (for more info check out the
Wikipedia page here*) to find the smallest monthly payment to the cent (no more multiples of
$10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how
fast it is. Produce the output in the same format as you did in problem 2.

*https://en.wikipedia.org/wiki/Bisection_method
"""

# Gather user input

balance = float(input("Enter the outstanding balance on your credit card: "))
interest_rate = float(input("Enter the anual credit card interest rate as a decimal: "))

# Calculate reasonable upper and lower bounds: 

lower = balance / 12.0
upper = (balance * (1 + (interest_rate / 12)) ** 12.0) / 12
set_balance = balance
print(balance)

while True:
    balance = set_balance
    payment = (lower + upper) / 2
    for month in range(1,13):
        balance *= interest_rate/12 + 1
        balance -= payment
    if balance > 0:
        lower = payment
    elif balance < -.02:
        upper = payment
    else:
        break
print("RESULT \nMonthly payment to pay off debt in 1 year: %.2f \
                \nNumber of months needed: %d \nBalance: %.2f" \
                        % (payment, month, balance))

