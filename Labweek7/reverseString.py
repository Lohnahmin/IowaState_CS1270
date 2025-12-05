#Lyle Osburne 10-16-2025
#Lab week 7 COMS 1270
#This code takes an input string and reverses it 5 different ways

def reverseStringV1(variable):

    reversed1 = variable[::-1]
    return reversed1


def reverseStringV2(variable):
    reversed2 = ("".join(reversed(variable)))
    return reversed2


def reverseStringV3(variable):
    reversed3 = ""
    for i in range(len(variable) -1, -1, -1):
        reversed3 += variable[i]
    return reversed3


def reverseStringV4(variable):
    reversed4 = ""
    for i in variable:
        reversed4 = i + reversed4
    return reversed4


def reverseStringV5(variable):
    reversed5 = ""
    i = len(variable) -1
    while i >= 0:
        reversed5 += variable[i]
        i -= 1
    return reversed5


def main():
    variable = input("Please provide a string: ")
    reversed1 = reverseStringV1(variable)
    print(reversed1)
    reversed2 = reverseStringV2(variable)
    print(reversed2)
    reversed3 = reverseStringV3(variable)
    print(reversed3)
    reversed4 = reverseStringV4(variable)
    print(reversed4)
    reversed5 = reverseStringV5(variable)
    print(reversed5)

if __name__ == "__main__":
    main()