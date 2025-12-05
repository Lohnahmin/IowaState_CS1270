# Lyle Osburne 10-9-2025
# Lab week 6 COM S 1270
# This function generates * each line adding 1 more per line
def starRightTriangle(num):
    for i in range(1, num +1):
        print('*' * i)
    print()

def main():
    num = int(input("Please enter a number: "))
    starRightTriangle(num)


if __name__ == "__main__":
    main()
