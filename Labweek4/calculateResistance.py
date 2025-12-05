# Lyle Osburne 9-25-2025
# Lab week 4 - This code is a function used to calculate resistance
# Ohm's law relates the electrical current (I) to the voltage difference (V) between two points of an electrical conductor.
# Formula: resistance = voltage / current

def calculateResistance(voltage,current):
    # Citation - URL: https://www.omnicalculator.com/physics/ohms-law-resistance
    # Citation - Date Posted: 06/11/2024
    # Citation - Date Acessed: 9-18-2025
    resistance = voltage / current
    return resistance

def main():
    voltage = int(input("enter a value for 'voltage':"))
    current = int(input("enter a value for 'current':"))
    resistance = calculateResistance(voltage,current)
    print("Value for voltage:",voltage)
    print("Value for current:",current)
    print(f"The resistance is {voltage} / {current} =", str(resistance),"ohms")

if __name__ == "__main__":
    main()