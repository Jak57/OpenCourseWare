# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 10:10:16 2021

@author: jakir
"""


annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

portion_down_payment = .25
down_payment = portion_down_payment * total_cost
current_savings = 0.0

r = 0.04 # Annual return
monthly_salary = annual_salary/12.0
monthly_salary_saved = monthly_salary * portion_saved
count = 0

while True:
    count += 1
    if (count-1)%6 == 0 and (count-1)>0:
        monthly_salary_saved += (monthly_salary_saved * semi_annual_raise)
        
    return_investment = (current_savings * r)/12.0
    current_savings += (return_investment + monthly_salary_saved)
    
    if current_savings >= down_payment:
        print("Number of months: " + str(count))
        break












