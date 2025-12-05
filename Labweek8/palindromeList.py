#Lyle Osburne
#10-30-2925
#Lab 7
# This function takes in a user input list and figures out if the list itself is a plaindrome

def userInput():
    list1 = []
    while True:
        list1.append(input("Pleaes enter a list of strings, press * to stop: "))
        if list1[-1] == "*":
            list1.pop()
            break

    return list1

def palindromeList(words):
    length = len(words)
    for i in range(length):
        if words[i] != words[length - 1 - i]:
            return False
    return True
        


def main():
    words = userInput()
    palindrome = palindromeList(words)
    print(palindrome)


if __name__ == "__main__":
    main()
       






