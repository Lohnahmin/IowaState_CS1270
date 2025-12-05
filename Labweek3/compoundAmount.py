# Lyle Osburne 9-18-2025
# Lab week 3 - This code is used to calculate accured interest gained over a certain time
# Formula: accrued_amount = principal * (1 + (rate/100) / number_compounds)**(number_compounds * time)
# Citation - URL: https://www.calculatorsoup.com/calculators/financial/compound-interest-calculator.php
# Citation - Author: Furey, Edward
# Citation - Date Posted: 08/01/2025
# Citation - Date Acessed: 09/18/2025

principal = int(input("enter a value for 'principal amount':"))
rate = int(input("enter a value for 'interest rate':"))
number_compounds = int(input("enter a value for 'number of times the interest compounds in a year':"))
time = int(input("enter a value for 'amount of years'"))

accrued_amount = principal * (1 + (rate/100) / number_compounds)**(number_compounds * time)
print("Value for principal:",principal)
print("Value for rate:",rate)
print("Value for 'number of times interest compounds':",number_compounds)
print("Value for 'amount of years' ")
print(f"The amount of accrued compounded interest is {principal} * (1 + ({rate}/100) / {number_compounds})**({number_compounds} * {time})", str(accrued_amount))