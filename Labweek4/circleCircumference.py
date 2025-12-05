import turtle
import random
import tridecagonTurtle

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
        newstr += applyRules(ch)
    return newstr

def applyRules(ch):
    if ch == 'F':
        return 'F-F++F-F'    # Koch snowflake edge
    elif ch == '+':
        return '+T'          # inject T after right turns
    elif ch == '-':
        return 'P-'          # inject P before left turns
    else:
        return ch

def drawLsystem(aTurtle, instructions, angle, distance, tri_side=28):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == 'T':
            x, y = aTurtle.position()
            tridecagonTurtle.tridecagonTurtle(tri_side, int(x), int(y), aTurtle)
        elif cmd == 'P':
            aTurtle.penup()
            aTurtle.goto(random.randint(-320, 320), random.randint(-240, 240))
            aTurtle.pendown()

def main():
    iters = 4
    axiom = "F+F+F"
    angle = 60
    distance = 4

    inst = createLSystem(iters, axiom)
    print(inst)  # will include T and P

    wn = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-280, 120)
    t.pendown()

    drawLsystem(t, inst, angle, distance, tri_side=28)
    wn.exitonclick()

if __name__ == "__main__":
    main()
