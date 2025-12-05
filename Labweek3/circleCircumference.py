# Lyle Osburne 9-12-2025
# Lab week 3 - This code is used to calculate the circumference of a circle
# The circumference of a circle is the perimeter of the circle. It is the total length of the boundary of the circle. 
# Formula: pi * radius
# Citation - URL: https://www.cuemath.com/geometry/circumference-of-a-circle/
# Citation - Date Acessed: 9-12-2025
import math
radius = int(input("enter a value for radius:"))

circumference = 2 * math.pi * radius
print("Value for radiusl",radius)
print(f"The area of the circle 2 x π x {radius} = " + str(circumference) + "ft" )
