import turtle

from numpy import angle
turtle.bgcolor("black")
turtle.pensize(5)
 
def rectangle(color):
    turtle.color(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.fd(650)
        turtle.right(90)
        turtle.fd(150)
        turtle.right(90)
    turtle.end_fill()
turtle.penup()
turtle.goto(-330,280)
turtle.pendown()
rectangle("orange")

turtle.penup()
turtle.goto(-330,120)
turtle.pendown()
rectangle("white")

turtle.penup()
turtle.goto(-330,-40)
turtle.pendown()
rectangle("green")

turtle.penup()
turtle.goto(50,50)
turtle.pendown()
turtle.left(90)
turtle.pencolor("blue")
turtle.circle(50)

turtle.penup()
turtle.goto(0,50)
turtle.pendown()
angle=15

for i in range (24):
    turtle.right(angle)
    turtle.fd(50)
    turtle.penup()
    turtle.goto(0,50)
    turtle.pendown()

turtle.exitonclick()

