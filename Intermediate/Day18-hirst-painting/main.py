import turtle as t
import random

# Use colorgram.py module to extract colors from a Hirst's painting

# import colorgram
# colors = colorgram.extract('image.jpg', 30)
#
# colors_list = []
# for color in colors:
#     colors_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
# print(colors_list)

# Delete the first color as it's the background color of the list
colors_list = [(232, 238, 246), (247, 238, 242), (239, 246, 243), (131, 166, 205), (222, 148, 106), (31, 42, 61),
               (199, 134, 147), (165, 59, 48), (140, 184, 162), (39, 105, 157), (238, 212, 89), (152, 58, 66),
               (217, 81, 70), (169, 29, 33), (236, 165, 156), (50, 112, 90), (35, 61, 55), (17, 97, 71), (156, 33, 30),
               (231, 160, 165), (53, 44, 49), (170, 188, 221), (57, 51, 48), (189, 100, 110), (31, 60, 109),
               (103, 127, 161), (34, 151, 209), (174, 200, 188), (65, 66, 56)]

# set the turtle attributes
shawn = t.Turtle()
shawn.shape("turtle")
shawn.speed("fastest")

t.colormode(255)


def draw_dot(times):
    """
    Draw given times of a dot with random color horizontally
    """
    for _ in range(times):
        shawn.dot(20, random.choice(colors_list))
        shawn.penup()
        shawn.forward(50)


# Set start position
shawn.penup()
x_start = -250
y_start = -250
shawn.setpos(x_start, y_start)

# Start drawing
for _ in range(10):
    draw_dot(10)
    y_start += 50
    shawn.setpos(x_start, y_start)
shawn.hideturtle()

# Screen settings
screen = t.Screen()
screen.exitonclick()
