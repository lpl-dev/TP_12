import turtle

def drawCurve(turtle,l):
    for i in range(4):
        turtle.forward(l)
        turtle.left(60) if i%2==0 else turtle.right(120)

turtle.setup(800, 400)
drawCurve(turtle, 40)
turtle.exitonclick()