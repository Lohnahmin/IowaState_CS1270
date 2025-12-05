# Lyle Osburne 09-25-2025
# Assignment #2
# The program will offer 3 options, Calculator, lucky number, and Quit
# Calcaulator will take inputs from the user for operators and integars and find the result
# Lucky number will ask the user for there favorite number and to pick a color, resulting in a lucky number!
# Quit will exit the program

import random

def calculator():
        operator = input("Please select an operator: [+] [-] [*] [/] [//] [%] [**]:")

        while operator != "+" and operator != "-" and operator != "*" and operator != "/" and operator != "//" and operator != "%" and operator != "**":
            operator = input("Error incorrect input please select one of the operators [+] [-] [*] [/] [//] [%] [**] ")
    
        num = int(input("Please input a integar:"))
        num_2 = int(input("Please enter a second integar:"))

        while operator == "/" and num_2 == 0 or operator == "//" and num_2 == 0 or operator == "%" and num_2 == 0:
            num_2 = int(input("Dividing by 0 is forbidden please select another integar:"))

        print(f"You first integar is: {num}")
        print(f"Your second integar is: {num_2}")

        if operator == "+":
            result = num + num_2
            print(f"The result calculation of {num} + {num_2} = {result}")
        elif operator == "-":
            result = num - num_2
            print(f"The result of calculation {num} - {num_2} = {result}")
        elif operator == "*":
            result = num * num_2
            print(f"The result of calculation {num} * {num_2} = {result}")
        elif operator == "/":
            result = num / num_2
            print(f"The result of calculation {num} / {num_2} = {result}")
        elif operator == "//":
            result = num // num_2
            print(f"The result of calculation {num} // {num_2} = {result}")
        elif operator == "%":
            result = num % num_2
            print(f"The result of calculation {num} % {num_2} = {result}")
        elif operator == "**":
            result = num ** num_2
            print(f"The result of calculation {num} ** {num_2} = {result}")

def luckynumber():
        favorite_num = int(input("Please input your favorite number:"))

        if favorite_num == 0:
            favorite_num  = 1

        if favorite_num >= 0:
            random_number = random.randint(0, favorite_num)
        else:
            random_number = random.randint(favorite_num, 0)

        color = input("Please pick a color: [Blue] [Purple] [Red] [Green] [Pink] [Black] [Orange]:")

        while color != "Blue" and color != "Purple" and color != "Red" and color != "Green" and color != "Pink" and color != "Black" and color != "Orange":
            color = input("Input errors please input [Blue] [Purple] [Red] [Green] [Pink] [Black] [Orange]:")

        if color == "Blue":
            lucky_num = random_number * 2
        elif color == "Purple":
            lucky_num = random_number * 3
        elif color == "Red":
            lucky_num = random_number * 4
        elif color == "Green":
            lucky_num = random_number * 5
        elif color == "Pink":
            lucky_num = random_number * 6
        elif color == "Black":
            lucky_num = random_number * 7
        elif color == "Orange":
            lucky_num = random_number * 8
            
        print(f"Your lucky number is {lucky_num}")

def main():
    print("Lucky Calculator!")
    print()
    print("By: Lyle Osburne")
    print("[COMS 1270-02]")
    operation = input("""What would you like to do?
    [c]: calculator, [l]: lucky number, [q]: quit:""")

    while operation != "c" and operation != "l" and operation != "q":
        operation = input("Input Error please select what you would like to do useing [c] [l] [q]:")

    if operation == "c":
        calculator()
    elif operation == "l":
        luckynumber()
    elif operation == "q":
        print("Quiting program")

if __name__ == "__main__":
    main()




