#Lyle Osburne
#10-30-2925
#Lab 7
#This function takes a user input list and rotates based on an input
def userInput():
    list1 = []
    while True:
        list1.append(input("Pleaes enter a list of numbers, press * to stop: "))
        if list1[-1] == "*":
            list1.pop()
            break

    return list1

def rotateList(int_list, rot):
    if rot > 0:
        for i in range(rot):
            last = int_list[-1]
            int_list.pop()
            int_list.insert(0, last)
    elif rot < 0:
        for i in range(-rot):
            first = int_list[0]
            int_list.pop(0)
            int_list.append(first)
    return int_list
    


def main():
    rot = int(input("Please enter a numer:"))
    int_list = userInput()
    print(rotateList(int_list, rot))

if __name__ == "__main__":
    main()
