# Lyle Osburne 10-9-2025
# Lab week 6 COM S 1270
# This fucnction generates lines with the same number used the same number of times

def sameNumberTriangle(num):
    for i in range(1,num+1):
        for j in range(i):
            print(i,end=" ")
        print()
def main():
    num = int(input("Please enter a number: "))
    sameNumberTriangle(num)

if __name__ == "__main__":
    main()