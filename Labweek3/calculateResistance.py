# Lyle Osburne 9-18-2025
# Lab week 3 - This code is used to calculate resistance
# Ohm's law relates the electrical current (I) to the voltage difference (V) between two points of an electrical conductor.
# Formula: resistance = voltage / current
# Citation - URL: https://www.omnicalculator.com/physics/ohms-law-resistance
# Citation - Author: Luis Hoyos
# Citation - Date Posted: 06/11/2024
# Citation - Date Acessed: 9-18-2025

voltage = int(input("enter a value for 'voltage':"))
current = int(input("enter a value for 'current':"))

resistance = voltage / current

print("Value for voltage:",voltage)
print("Value for current:",current)
print(f"The resistance is {voltage} / {current} =", str(resistance),"ohms")