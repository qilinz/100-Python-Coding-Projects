import turtle as t
import random
# Turtle attributes
shawn = t.Turtle()
shawn.shape("turtle")
shawn.color("DodgerBlue")
shawn.speed("fastest")
t.colormode(255)


# Challenge 1: Draw a Square
# for i in range(4):
#     shawn.forward(100)
#     shawn.right(90)

# Challenge 2: Draw a Dashed Line
# for i in range(15):
#     shawn.forward(10)
#     shawn.penup()
#     shawn.forward(10)
#     shawn.pendown()


# Challenge 3: Draw different shapes
def draw_shape(side):
    angle = 360 / side
    for _ in range(side):
        shawn.forward(100)
        shawn.right(angle)


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    shawn.pencolor(r, g, b)
#
#
# shape_side = 3  # start from triangle
# while shape_side < 11:
#     draw_shape(shape_side)
#     shape_side += 1
#     change_color()


# Challenge 4: Draw a random Walk
def random_walk():
    angle = [0, 90, 180, 270]
    shawn.setheading(random.choice(angle))
    shawn.forward(20)


# i = 1
# shawn.pensize(10)
# while i < 200:
#     random_walk()
#     change_color()
#     i += 1


# Challenge 5: Make a Spirograph
i = 0
while i <= 72:
    shawn.circle(100)
    shawn.setheading(5*i)
    change_color()
    i += 1


# Screen settings
screen = t.Screen()
screen.exitonclick()
