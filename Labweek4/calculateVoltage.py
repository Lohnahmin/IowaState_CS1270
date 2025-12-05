# Base code adapted from Runestone Interactive, Example 9.15.2 (accessed 2025-09-25)

import turtle
import random
from tridecagonTurtle import tridecagonTurtle

def createLSystem(numIters, axiom):
    startString = axiom
    endString = ""
    for _ in range(numIters):
        endString = processString(startString)
        startString = endString
    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)
    return newstr

def applyRules(ch):
    if ch == 'F':
        return 'PT+PT-PT'
    elif ch in ('T', 'P', '+', '-', 'B'):
        return ch
    else:
        return ch

def drawLsystem(aTurtle, instructions, angle, distance, tri_side=18):
    for cmd in instructions:
        if cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == 'P':
            scr = aTurtle.getscreen()
            half_w = scr.window_width() // 2 - 40
            half_h = scr.window_height() // 2 - 40
            wasdown = aTurtle.isdown()
            aTurtle.penup()
            aTurtle.goto(random.randint(-half_w, half_w), random.randint(-half_h, half_h))
            if wasdown:
                aTurtle.pendown()
        elif cmd == 'T':
            pos = aTurtle.position()
            head = aTurtle.heading()
            wasdown = aTurtle.isdown()
            aTurtle.penup()
            aTurtle.setheading(0)
            tridecagonTurtle(tri_side, pos[0], pos[1], aTurtle)
            aTurtle.penup()
            aTurtle.goto(pos)
            aTurtle.setheading(head)
            if wasdown:
                aTurtle.pendown()
        else:
            pass

def main():
    inst = createLSystem(3, "F+F+F")
    print(inst)
    t = turtle.Turtle()
    wn = turtle.Screen()
    t.speed(0)
    t.up(); t.back(wn.window_width() // 3); t.down()
    drawLsystem(t, inst, 75, 10, tri_side=20)
    wn.exitonclick()

if __name__ == "__main__":
    main()
