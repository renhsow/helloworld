def plotParabola(myTurtle):
    myTurtle.up()
    myTurtle.goto(-20,400)
    myTurtle.down()
    for x in range(-20,21,1):
        y = x**2
        myTurtle.goto(x,y)
