import turtle
import random
chin = turtle.Turtle()
chin.shape("arrow")
colours = ["lime green", "aquamarine", "plum", "cyan", "dark orchid", "yellow", "red"]
d = 10
def black_hole():
    chin.color(random.choice(colours))
    chin.pensize(2)
    chin.circle(d)
    chin.speed(10)
    chin.left(20)
while True:
    for i in range(0, 11):
        black_hole()
        d = d + 4



