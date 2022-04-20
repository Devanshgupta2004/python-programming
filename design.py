import turtle
turtle.bgcolor("black")
turtle.speed(100)
turtle.pensize(2)

turtle.pencolor("purple")

def drawcircle(radius):
    for i in range (10):
        turtle.circle(radius)
        radius-=4

def design():
    for i in range(10):
        drawcircle(150)
        turtle.right(36)

design()
turtle.exitonclick()                
