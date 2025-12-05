# Lyle Osburne 9-25-2025
# Lab week 4 - This code is a function used to take user input and generate random numbers and find the product of them

import random

def randomProduct(a, b, c):
    product = 1
    for i in range(a):
        num = random.randrange(b, c + 1)
        product *= num
        print(f"Random number {i+1}: {num}")
    return product

def main():
    a = int(input("Please enter a number:"))
    b = int(input("Please enter a number:"))
    c = int(input("Please enter a number:"))
    result = randomProduct(a, b, c)
    print(f"Final product: {result}")
    
if __name__ == "__main__":
    main()