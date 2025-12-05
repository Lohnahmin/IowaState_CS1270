# Lyle Osburne 9-25-2025
# Lab week 4 - This code is a function used to take user input and generate random numbers and find the product of them

def sqrtIter(x,iterations):
    # CITATION - URL:https://www.cuemath.com/algebra/square-root-of-2/
    # CITATION - Date Accessed: 9-25-2025
    y_0 = 1
    y = ((x / y_0) + y_0) / 2
    print(f"Iteration 1 = {y}")
    for i in range(1, iterations):
        y = ((x / y) + y) / 2
        print(f"Iteration {i+1} = {y}")
    return y


def main():
    x = int(input("Please enter a number:"))
    iterations = int(input("Please enter a number:"))
    result = sqrtIter(x,iterations)

    print(f"Final approximation of sqrt({x}): {result}")

if __name__ == "__main__":
    main()
