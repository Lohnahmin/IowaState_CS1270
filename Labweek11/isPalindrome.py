# Your Name
# Date
# Lab 11 - isPalindrome.py
# This file checks if a string is a palindrome in two ways: one with a loop and
# one using recursion.

def isPalindromeIterative(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def isPalindromeRecursive(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return isPalindromeRecursive(s[1:-1])

def main():
    x = input("Please enter a string: ")
    print(isPalindromeIterative(x))
    print(isPalindromeRecursive(x))

if __name__ == "__main__":
    main()