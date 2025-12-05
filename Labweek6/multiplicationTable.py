# Lyle Osburne 10-9-2025
# Lab week 6 COM S 1270
# This function generates a multiplication table

def multiplicationTable(lowNum,highNum):
    for i in range(lowNum, highNum +1):
        for j in range(lowNum,highNum +1):
            print(i * j, end=" ")
        print()
           

        
        
def main():
     lowNum = int(input("Please select a number between 1-10:"))
     highNum = int(input("Please select a number between 1-10:"))
     table = multiplicationTable(lowNum,highNum)
    #  print(table)

if __name__ == "__main__":
    main()
