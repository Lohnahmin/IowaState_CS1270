# Lyle Osburne 9-19-2025
# Lab week 5 - This program takes the user input as a year and calculates if it is a leap year


def leapyear(year):
    if year % 4 == 0:
        leap_year = True
    else:
        leap_year = False
    return leap_year

def main():
    year = int(input("Please input a year:"))
    leap_year = leapyear(year)
    print(leap_year)
if __name__ == "__main__":
    main()


