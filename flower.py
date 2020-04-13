import turtle
import random
masechka = turtle.Turtle()
colours = ["red", "dark orchid", "aquamarine", "hot pink"]
masechka.speed(5)
def flower():
    masechka.penup()
    masechka.forward(10)
    masechka.pendown()
    masechka.pensize(2)
    masechka.color(random.choice(colours))
    for i in range(0, 8):
        masechka.circle(6)
        masechka.right(45)
        masechka.penup()
        masechka.forward(5)
        masechka.pendown()
    masechka.right(135)
    masechka.penup()
    masechka.forward(7)
    masechka.pendown()
    masechka.color("goldenrod")
    masechka.pensize(10)
    masechka.circle(2)
flower()