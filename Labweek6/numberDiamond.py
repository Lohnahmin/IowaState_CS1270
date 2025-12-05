# Lye Osburne 10-9-2025
# Lab 6 COM S 1270
# This function takes a user input and generates a diamond shape

def numberDiamond(num):
    for i in range(1, num + 1):
        print(" " * (num - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    
    for i in range(num - 1, 0, -1):
        print(" " * (num - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def main():
    num = int(input("Enter a number: "))
    numberDiamond(num)

if __name__ == "__main__":
    main()