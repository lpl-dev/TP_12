import turtle

def drawCurve(turtle,l,n):
    if n<=0:
        turtle.forward(l)
        return
    for i in range(4):
        drawCurve(turtle, l/3, n-1)
        (turtle.left(60) if i % 2 == 0 else turtle.right(120)) if i!=3 else ''

def drawFullCurve(turtle,l,n):
    for _ in range(3):
        drawCurve(turtle,l,n)
        turtle.right(120)

turtle.setup(800, 600)
turtle.penup()
turtle.goto(-200,100)
turtle.pendown()
drawFullCurve(turtle, 300, 2)
turtle.ht()
turtle.exitonclick()