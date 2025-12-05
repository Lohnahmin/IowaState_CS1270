# Lyle Osburne 9-12-2025
# Lab week 3 - This code is used to calculate the perieter of a rectangle
# The perimeter of a rectangle is the total length or distance of its boundary on all sides.
# Formula: perimeter = 2 * (length + width)
# Citation - URL: https://www.cuemath.com/measurement/perimeter-of-a-rectangle/
# Citation - Date Acessed: 9-12-2025

length = int(input("enter a value for 'length':"))
width = int(input("enter a value for 'width' :"))


perimeter = 2 *(length + width)
print("Value for length:",length)
print("Value for width:",width)
print(f"The perimeter of the rectangle is 2 x ({length} x {width}) = " + str(perimeter) + "ft")