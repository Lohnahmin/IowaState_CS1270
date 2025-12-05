#Lyle Osburne 10-16-2025
#Lab week 7 COMS 1270
#This code takes an input string and utilizes an import module from reverseString.py to check if it is a palindrome

import reverseString

def palindromeCheckV1(palindrome):
    check_palindrome = reverseString.reverseStringV1(palindrome)
    if palindrome == check_palindrome:
        print(palindrome, "is a palindrome")
    else:
        print(palindrome, "is not a palindrome")
    return check_palindrome
def palindromeCheckV2(palindrome):
    check_palindrome = reverseString.reverseStringV1(palindrome)
    for i in range(len(palindrome)):
        if palindrome[i] != check_palindrome[i]:
            print(palindrome, "is not a palindrome")
            return
        
    print(palindrome, "is a palindrome")

def main():
    palindrome = input("Please enter a palindrome: ")
    palindromeCheckV1(palindrome)
    palindromeCheckV2(palindrome)

if __name__ == "__main__":
    main()