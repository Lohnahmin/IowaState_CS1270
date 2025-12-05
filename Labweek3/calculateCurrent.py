# Lyle Osburne 9-18-2025
# Lab week 3 - This code is used calculate current
# Ohm's Law states that the voltage (V) across a conductor is equal to the product of the current (I) flowing through it and the resistance (R) of the conductor. According to Ohm's law, the current is the ratio of the potential difference (voltage) and the resistance. Thus, the electric current formula is given by: I = V/R
# Formula: current = voltage / resistance
# Citation - URL: https://www.cuemath.com/current-formula/
# Citation - Date Acessed: 9-18-2025

voltage = int(input("enter a value for 'voltage':"))
resistance = int(input("enter a value for 'resistance':"))

current = voltage / resistance

print("Value for voltage:",voltage)
print("Value for current:",current)
print(f"The resistance is {voltage} / {resistance} =", str(current),"amperes")