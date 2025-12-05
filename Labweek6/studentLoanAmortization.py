# Lyle Osburne 10-9-2025
# Lab week 6 COM S 1270
# This function calculates the payment on a monthly loan from remaining balance repeatedly

def studentLoanAmortization(principal, yearlyInterestRate, numberOfYears):
    monthlyRate = yearlyInterestRate / 12
    numberOfMonths = numberOfYears * 12

    monthlyPayment = (principal * monthlyRate * (1 + monthlyRate) ** numberOfMonths) / ((1 + monthlyRate) ** numberOfMonths - 1)

    balance = principal

    print(f"{'Period':<8}{'Total Payment Due':<20}{'Computed Interest Due':<25}{'Principal Due':<20}{'Principal Balance':<20}")
    print("-" * 100)

    for period in range(1, numberOfMonths + 1):
        interest = balance * monthlyRate
        principalDue = monthlyPayment - interest
        balance -= principalDue
        if balance < 0:
            balance = 0
        print(f"{period:<8}{monthlyPayment:<20.2f}{interest:<25.2f}{principalDue:<20.2f}{balance:<20.2f}")

def main():
    principal = float(input("Enter the loan principal: "))
    yearlyInterestRate = float(input("Enter the yearly interest rate (as a decimal: "))
    numberOfYears = int(input("Enter the number of years: "))
    studentLoanAmortization(principal, yearlyInterestRate, numberOfYears)

if __name__ == "__main__":
    main()