#Lyle Osburne 10-16-2025
#Lab week 7 COMS 1270
#This takes a string and a substring and finds if they are in and what index it starts at

def findSubStringV1(string, substring):
    index = string.find(substring)
    if index != -1:
        return index
    return -1


def findSubStringV2(string, substring):
    if substring in string:
        index = string.index(substring)
        return index
    else:
        return -1


def findSubStringV3(string, substring):
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            return i
    return -1


def main():
    string = input("Please provide a string: ")
    substring = input("Please provide a substring: ")

    result1 = findSubStringV1(string, substring)
    print("Version 1:", result1)

    result2 = findSubStringV2(string, substring)
    print("Version 2:", result2)

    result3 = findSubStringV3(string, substring)
    print("Version 3:", result3)


if __name__ == "__main__":
    main()