# Lyle Osburne 9-12-2025
# Lab week 3 - This code is used to calculate the area of a circle
# The area of a circle is the amount of space enclosed within the boundary of a circle.
# Formula: pi * (radius ** 2)
# Citation - URL: https://www.cuemath.com/geometry/area-of-a-circle/
# Citation - Date Acessed: 9-12-2025
import math
radius = int(input("enter a value for 'radius':"))

area = math.pi * (radius ** 2)
print("Value for radius:",radius)
print(f"The area of the circle is π x ({radius} ** {2}) = " + str(area) + 'ft' )