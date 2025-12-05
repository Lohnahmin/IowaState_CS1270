# Lyle Osburne 9-18-2025
# Lab week 3 - This code is used to calculate the annual percentage rate on a loan
# Formula: apr = (((interest_charges + fees) / loan_amount) / days_in_term) * 100
# Citation - URL: https://www.investopedia.com/terms/a/apr.asp
# Citation - Author: Jason Fernando
# Citation - Date Posted: 08/13/2025
# Citation - Date Acessed: 09/18/2025

interest_charges = int(input("enter a value for 'interest charges':"))
fees = int(input("enter a value for 'fees':"))
loan_amount = int(input("enter a value for 'loan amount':"))
days_in_term = int(input("enter a value for 'days in term':"))

apr = (((interest_charges + fees) / loan_amount) / days_in_term) * 100

print("value for interest_charges:",interest_charges)
print("Value for fees:",fees)
print("Value for loan_amount:",loan_amount)
print("Value for days_in_term",days_in_term)
print(f"The APR calculated is ((({interest_charges} + {fees}) / {loan_amount}) /  {days_in_term}) =", str(apr),"%")