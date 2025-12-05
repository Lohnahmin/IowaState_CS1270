# Lyle Osburne 9-19-2025
# Lab week 4 - This code is utilizes a function to calculate the square units of a rectangle
# The area of a rectangle is the region occupied by a rectangle within its boundary is defined as the area of the rectangle.
# Formula: area = base * height

def areaOfRectangle(base, height):
    # Citation - URL: https://www.cuemath.com/measurement/area-of-rectangle/
    # Citation - Date Accessed: 9-12-2025
    area = base * height
    return area

def main():

    base = int(input("enter a value for 'base':"))
    height = int(input("enter a value for 'height':"))
    area = areaOfRectangle(base, height)
    print("Value for base:",base)
    print("Value for height:",height)
    print(f"The area of the rectangle is {base} x {height} = " + str(area) + " square units")

if __name__ == "__main__":
    main()