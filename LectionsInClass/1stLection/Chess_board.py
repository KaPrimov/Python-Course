import turtle
side = 40
y = 40
for j in range(8):
    for i in range(8):
        if j % 2 == 0:
            if i % 2 == 0:
                turtle.begin_fill()
        if j % 2 == 1:
            if i % 2 == 1:
                turtle.begin_fill()
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.end_fill()
        turtle.forward(side)
        turtle.left(90)
        turtle.end_fill()
        turtle.forward(side)
        if i == 7 or i == 15 or i == 23 or i == 31 or i == 39 or i == 47 or i == 55 or i == 63:
            x = 0
            turtle.penup()
            turtle.goto(x,y)
            turtle.pendown()
            y += 40

turtle.exitonclick()
