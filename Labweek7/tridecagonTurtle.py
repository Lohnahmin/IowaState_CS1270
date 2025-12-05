# Lyle Osburne 9-25-2025
# Lab week 4 - This function utilizes the turtle modeule to generate a tridecagon based on user inputs

import turtle

def tridecagonTurtle(s,x,y,t):
    # CITATION - URL:https://en.wikipedia.org/wiki/Tridecagon
    # CITATION - Date posted/edited: 09/21/2025
    # CITATION - Date Accessed: 9-25-2025
    t.penup()
    t.goto(x, y)
    t.pendown()

    sides = 13
    angle = 360/sides

    for i in range(sides):
        t.forward(s)
        t.left(angle)
    
def main():
        s = int(input("Enter the side length: "))
        x = int(input("Enter the starting x coordinate: "))
        y = int(input("Enter the starting y coordinate: "))

        screen = turtle.Screen()
        t = turtle.Turtle()
        t.speed()
        tridecagonTurtle(s,x,y,t)
        screen.mainloop()
    
if __name__ == "__main__":
        main()
