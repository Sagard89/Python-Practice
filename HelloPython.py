import turtle

def drawShapeUsingSquare(someTurtle,squareSide):
    i=0
    for i in range(180):
        drawSquare(someTurtle,squareSide)
        someTurtle.right(10)
        print("Value of i ", i)
        squareSide += 1
        print("Value of squareSide ", squareSide)

def drawSquare(someTurtle,squareSide):
    i=0
    for i in range(4):
       someTurtle.forward(squareSide)
       someTurtle.right(90)

def initTurtle():
    window = turtle.Screen()
    window.bgcolor("Yellow")
    squareSideLength = 10
    turtle1 = turtle.Turtle()
    turtle1.shape("turtle")
    drawShapeUsingSquare(turtle1,squareSideLength)

initTurtle()
