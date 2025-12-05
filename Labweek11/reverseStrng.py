# Your Name
# Date
# Lab 11 - reverseString.py
# This file reverses a string in two different ways. One uses a loop starting
# from the end of the string, and the other uses recursion.

def reverseIterative(s):
    result = ""
    i = len(s) - 1
    while i >= 0:
        result += s[i]
        i -= 1
    return result

def reverseRecursive(s):
    if len(s) <= 1:
        return s
    return reverseRecursive(s[1:]) + s[0]

def main():
    testVal = input("Please Enter a String: ")
    answer1 = reverseIterative(testVal)
    print("Iterative:", answer1)
    answer2 = reverseRecursive(testVal)
    print("Recursive:", answer2)

if __name__ == "__main__":
    main()