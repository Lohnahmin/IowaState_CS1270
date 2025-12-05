# Lyle Osburne 9-25-2025
# Lab week 4 - This code is a function used to calculate the annual percentage rate on a loan
# Formula: apr = (((interest_charges + fees) / loan_amount) / days_in_term) * 100

def annualPercentageRate(interest_charges,fees,loan_amount,days_in_term):
    # Citation - URL: https://www.investopedia.com/terms/a/apr.asp
    # Citation - Date Posted: 08/13/2025
    # Citation - Date Acessed: 09/18/2025
    apr = (((interest_charges + fees) / loan_amount) / days_in_term) * 100
    return apr

def main():
    interest_charges = int(input("enter a value for 'interest charges':"))
    fees = int(input("enter a value for 'fees':"))
    loan_amount = int(input("enter a value for 'loan amount':"))
    days_in_term = int(input("enter a value for 'days in term':"))
    apr = annualPercentageRate(interest_charges,fees,loan_amount,days_in_term)
    print("value for interest_charges:",interest_charges)
    print("Value for fees:",fees)
    print("Value for loan_amount:",loan_amount)
    print("Value for days_in_term",days_in_term)
    print(f"The APR calculated is ((({interest_charges} + {fees}) / {loan_amount}) /  {days_in_term}) =", str(apr),"%")

if __name__ == "__main__":
    main()