# Lyle Osburne 9-18-2025
# Lab week 3 - This code is used to calculate voltage
# Ohm’s Law Equation: V = IR, where V is the voltage across the conductor, I is the current flowing through the conductor and R is the resistance provided by the conductor to the flow of current.
# Citation - URL: https://byjus.com/physics/ohms-law/
# Citation - Date Acessed: 9-18-2025

current = int(input("enter a value for 'current':"))
resistance = int(input("enter a value for 'resistance':"))

voltage = current * resistance 

print("Value for current:",current)
print("Value for resistance:",resistance)
print(f"The voltage is {current} x {resistance} =", str(voltage), "volts")