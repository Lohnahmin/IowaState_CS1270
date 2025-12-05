#Lyle Osburne
#10-30-2925
#Lab 7
#This function take user input as a list of strings, then compares a num to this list finds it and puts it at the end
def userInput():
    list1 = []
    while True:
        list1.append(input("Pleaes enter a list of numbers, press * to stop: "))
        if list1[-1] == "*":
            list1.pop()
            break

    return list1

def endNum(int_list, num):
    for i in int_list:
        if i == str(num):
            int_list.remove(i)
            int_list.append(i)
    return int_list
def main():
    int_list = userInput()
    num = int(input("Please enter a number:"))
    result = endNum(int_list, num)
    print(result)

if __name__ == "__main__":
    main()
