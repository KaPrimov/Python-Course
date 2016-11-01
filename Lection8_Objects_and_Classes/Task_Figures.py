from turtle import Turtle, done as turtle_done


def main():
    t = Turtle()
    t.speed("slow")
    figures = create_figures(FIGURES_INPUT_DATA)
    # figures = [
    #     Circle(0, 0, radius=100, color='green'),
    #     SquareEasiest(0, 0, radius=100, color='red')
    # ]
    for figure in figures:
        figure.draw(t)

    turtle_done()

# ========================================================

FIGURES_INPUT_DATA = [
    {"type": "square", "center_x": 0, "center_y": 0, "side": 2, "color": "black"},
    {"type": "triangle", "center_x": 0, "center_y": 0, "side": 200, "color": "brown"},
    {"type": "square", "center_x": 0, "center_y": 0, "side": 100, "color": "red"},
    {"type": "square", "center_x": 0, "center_y": 0, "side": 200, "color": "blue"},
    {"type": "rectangle", "center_x": 0, "center_y": 0, "side_a": 200, "side_b": 50, "color": "blue"},
    {"type": "circle", "center_x": 0, "center_y": 0, "radius": 50, "color": "blue"},
    {"type": "triangle", "center_x": 0, "center_y": 0, "side": 250, "color": "yellow"},
    {"type": "circle", "center_x": 0, "center_y": 0, "radius": 100, "color": "red"}
]


class Figure:

    def __init__(self, center_x: int, center_y: int, color: str):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.color = color

    def __str__(self):
        return "Figure : ({}, {})".format(self.center_x, self.center_y)

    def draw(self, turtle):
        turtle.color(self.color)

    def jump_to(self, turtle, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()


class Circle(Figure):
    steps = None

    def __init__(self, center_x: int=0, center_y: int=0, radius: int=0, color: str='black'):
        super().__init__(center_x, center_y, color)
        self.radius = radius


    def draw(self, turtle: Turtle):
        super().draw(turtle)
        self.jump_to(turtle, self.center_x, self.center_y - self.radius)
        turtle.circle(self.radius, steps=self.steps)
        self.jump_to(turtle, 0, 0)


class SquareEasy(Circle):
    def __init__(self, center_x: int=0, center_y: int=0, radius: int=0, color: str='black'):
        super().__init__(center_x, center_y, radius, color)
        self.steps = 4


class SquareEasiest(Circle):
    steps = 4


class Square(Figure):

    def __init__(self, center_x: int=0, center_y: int=0, side: int=0, color: str='black'):
        super().__init__(center_x, center_y, color)
        self.side = side

    def draw(self, turtle: Turtle):
        super().draw(turtle)
        self.jump_to(turtle,
                     self.center_x - self.side/2,
                     self.center_y - self.side/2)

        for _ in range(4):
            turtle.forward(self.side)
            turtle.left(90)

        self.jump_to(turtle, 0, 0)


class Triangle(Figure):

    def __init__(self, center_x: int=0, center_y: int=0, side: int=0, color: str='black'):
        super().__init__(center_x, center_y, color)
        self.side = side

    def draw(self, turtle: Turtle):
        super().draw(turtle)
        self.jump_to(turtle,
                     self.center_x - self.side/2,
                     self.center_y - self.side/3)

        for _ in range(3):
            turtle.forward(self.side)
            turtle.left(120)

        self.jump_to(turtle, 0, 0)


class Rectangle(Figure):

    def __init__(self, center_x: int=0, center_y: int=0, side_a: int=0, side_b: int=0, color: str='black'):
        super().__init__(center_x, center_y, color)
        self.side_a = side_a
        self.side_b = side_b

    def draw(self, turtle: Turtle):
        super().draw(turtle)
        self.jump_to(turtle,
                     self.center_x - self.side_a/2,
                     self.center_y - self.side_b/2)

        turns = 4
        for _ in range(turns):
            if turns % 2 == 0:
                turtle.forward(self.side_a)
                turtle.left(90)
            elif turns % 2 != 0:
                turtle.forward(self.side_b)
                turtle.left(90)
            turns+=1

        self.jump_to(turtle, 0, 0)


def create_figures(figures_input_data: list) -> list:
    """
    Return a list of Figure instances
    :param figures_list:
    :return:
    """
    result = []
    for fdata in figures_input_data:
        type = fdata['type']
        if type == 'square':
            figure = Square(
                center_x=fdata['center_x'],
                center_y=fdata['center_y'],
                side=fdata['side'],
                color=fdata['color'],
            )
        elif type == 'circle':
            figure = Circle(
                center_x=fdata['center_x'],
                center_y=fdata['center_y'],
                radius=fdata['radius'],
                color=fdata['color'],
            )
        elif type == 'triangle':
            figure = Triangle(
                center_x=fdata['center_x'],
                center_y=fdata['center_y'],
                side=fdata['side'],
                color=fdata['color']
            )
        elif type == 'rectangle':
            figure = Rectangle(
                center_x=fdata['center_x'],
                center_y=fdata['center_y'],
                side_a=fdata['side_a'],
                side_b=fdata['side_b'],
                color=fdata['color']
            )
        else:
            raise Exception("Unsupported figure type: " + type)
        result.append(figure)

    return result

if __name__ == '__main__':
    main()