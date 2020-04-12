import turtle
import random
chin = turtle.Turtle()
d = 10
colours = ["red", "yellow", "dark orchid", "aquamarine", "cyan", "goldenrod", "lime green", "hot pink"]
def black_hole():
    chin.color(random.choice(colours))
    chin.shape("arrow")
    chin.speed(10)
    for i in range(0, 3):
        chin.forward(d)
        chin.left(120)
    chin.left(20)
while True:
    black_hole()
    d = d + 5
