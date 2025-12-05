# Lyle Osburne  
# 12/04/2025
# Lab 11s
# This program runs FizzBuzz with an extra check for Bazz (multiples of 7).
# One function uses normal if-statements and the other uses a simple dictionary.

def fizzBuzzModulus(n):
    result = []
    for i in range(1, n + 1):
        s = ""
        if i % 3 == 0:
            s += "Fizz"
        if i % 5 == 0:
            s += "Buzz"
        if i % 7 == 0:
            s += "Bazz"
        if s == "":
            s = str(i)
        result.append(s)
    return result

def fizzBuzzDict(n):
    result = []
    for i in range(1, n + 1):
        words = {}

        if i % 3 == 0:
            words["Fizz"] = 1
        if i % 5 == 0:
            words["Buzz"] = 1
        if i % 7 == 0:
            words["Bazz"] = 1

        if len(words) == 0:
            result.append(str(i))
        else:
            s = ""
            for w in words:
                s += w
            result.append(s)

    return result

def main():
    n = int(input("Enter an integer: "))
    print(fizzBuzzModulus(n))
    print(fizzBuzzDict(n))

if __name__ == "__main__":
    main()