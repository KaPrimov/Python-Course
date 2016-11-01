side = int(input("Side: "))

import turtle
turtle.speed('fast')

colors = ['red']

for a in range(1):
    turtle.color(colors[a])

    for b in range(4):
        turtle.forward(side)
        turtle.right(90)

turtle.done()
