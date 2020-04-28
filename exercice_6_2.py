import turtle

def drawCurve(turtle,l,n):
    if n<=0:
        turtle.forward(l)
        return
    for i in range(4):
        drawCurve(turtle, l / 3, n - 1)
        (turtle.left(60) if i % 2 == 0 else turtle.right(120)) if i!=3 else ''

turtle.setup(800, 400)
turtle.setworldcoordinates(-1,-1,800,400)
drawCurve(turtle, 300, 3)
turtle.ht()
turtle.exitonclick()