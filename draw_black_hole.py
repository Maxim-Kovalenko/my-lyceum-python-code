import turtle
import random
chin = turtle.Turtle()
chin.shape("arrow")
colours = ["lime green", "aquamarine", "plum", "cyan", "dark orchid", "yellow", "red"]
d = 10
def black_hole():
    chin.color(random.choice(colours))
    chin.pensize(random.randint(1, 10))
    chin.circle(d)
while True:
    for  i in range(0,11):
        black_hole()
        d = d + 4



