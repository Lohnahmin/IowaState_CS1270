# Lyle Osburne 9-19-2025
# Lab week 4 - This code is utilizes a function to calculate the perieter of a rectangle
# The perimeter of a rectangle is the total length or distance of its boundary on all sides.
# Formula: perimeter = 2 * (length + width)

def rectanglePerimeter(length, width):
    # Citation - URL: https://www.cuemath.com/measurement/perimeter-of-a-rectangle/
    # Citation - Date Ac essed: 9-12-2025
    perimeter = 2 * (length + width)
    return perimeter

def main():

    length = int(input("enter a value for 'length':"))
    width = int(input("enter a value for 'width' :"))
    perimeter = rectanglePerimeter(length, width)
    print("Value for length:",length)
    print("Value for width:",width)
    print(f"The perimeter of the rectangle is 2 x ({length} x {width}) = " + str(perimeter) + "ft")

if __name__ == "__main__":
    main()