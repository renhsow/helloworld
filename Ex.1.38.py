def drawSquare(myTurtle,sideLength):
    myTurtle.forward(sideLength)
    myTurtle.left(90)
    myTurtle.forward(sideLength)
    myTurtle.left(90)
    myTurtle.forward(sideLength)
    myTurtle.left(90)
    myTurtle.forward(sideLength)
    myTurtle.left(90)
def drawNestedSquares(myTurtle):
    for i in range(200,200-5*10,-5):
        drawSquare(myTurtle,i)
