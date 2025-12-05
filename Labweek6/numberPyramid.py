# Lyle Osburne 10-9-2025
# Lab week 6 COM S 1270
# this function generates half a diamond in numbers

def numberPyramid(num):
    for i in range(1, num + 1):
        print(" " * (num - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
def main():
    num = int(input("Please enter a number: "))
    numberPyramid(num)

if __name__ == "__main__":
    main()
