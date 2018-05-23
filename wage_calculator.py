# wage_calculator.py - Jeff Hritz
"""
This module gathers inputs and calculates your paycheck based on your hourly wage, how many hours you work,
tax rates, and pay-check deductions.
"""

pay_rate = int(input("Pay rate: "))
hours_worked = float(input("Hours worked: "))
tax_rate = float(.1981)
deductions = float(6.47)
gross_pay = (hours_worked * pay_rate)
total_deduction = ((gross_pay * tax_rate) - deductions)
net_pay = (gross_pay - total_deduction)
print("-----------")
print("Here are your paycheck details:")
print("Pay rate - %s" % round(pay_rate, 2))
print("Hours work - %s" % hours_worked)
print("Tax Rate - %s" % (tax_rate * 100) + "%")
print("Deductions - %s" % "$" + str(deductions))
print("==")
print("Gross Pay - %s" % "$" + str(gross_pay))
print("Net Pay - %s" % "$" + str(net_pay))


