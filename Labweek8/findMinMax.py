def makeList(num):
    while "*" not in num:
        num2 = input("Please enter numbers, when you are done enter *: ")
        num.append(num2)
    num.pop()
    return num

def findMin(int_num):
    min_num = int_num[0]
    for i in int_num:
        if i < min_num:
            min_num = i
    return print(f"the minimum number in the list i: {min_num}")

def findMax(int_num):
    max_num = int_num[0]
    for i in int_num:
        if i > max_num:
            max_num = i
    return print(f"The Max number in the list is L: {max_num}")

def main():
    num = []
    makeList(num)
    int_num = list(map(int, num))
    findMin(int_num)
    findMax(int_num)
    
if __name__ == "__main__":
    main()

