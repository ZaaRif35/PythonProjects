from turtle import Turtle, Screen
import random
from random import randint

screen = Screen()
screen.setup(1920, 1080, 0, 0)

t = Turtle()
t.color("red")
t.speed(0)

s = Turtle()
s.color("black")
s.speed(0)

# Ego-Perspektive

t.up()
t.goto(-950, -450)
t.down()

t.color("#DFCBAF")
t.begin_fill()
t.goto(950, -450)
t.goto(999.01, -0.99)
t.goto(-400.99, -0.99)
t.goto(-950, -450)
t.end_fill()

t.color("#d28c5b")
t.begin_fill()
t.up()
t.goto(-950, -450)
t.down()
t.goto(-950, 510)
t.goto(670, 510)
t.goto(670, -1)
t.goto(-498.5, -1)
t.goto(-950, -450)
t.end_fill()

t.color("black")
t.goto(-950, 510)
t.goto(670, 510)
t.goto(670, -1)
t.goto(-498.5, -1)
t.goto(-950, -450)
t.up()
t.goto(-498.5, -1)
t.down()
t.setheading(90)
t.forward(500)

t.up()
t.goto(-415, 60)
t.down()
t.setheading(0)
t.color("#000c1a")
t.begin_fill()
for x in range(2):
    t.forward(1000)
    t.left(90)
    t.forward(290)
    t.left(90)
t.end_fill()

t.up()
t.goto(-415, 60)
t.down()
t.setheading(0)
t.color("black")
t.width(5)
for x in range(2):
    t.forward(1000)
    t.left(90)
    t.forward(290)
    t.left(90)
t.up()
t.goto(85, 60)
t.down()
t.setheading(90)
t.forward(290)


def himmel1():
    s.up()
    s.goto(random.randint(-400, 570), random.randint(100, 360))
    s.down()
    s.dot(5, "#DFE6FF")


def himmel2():
    s.up()
    s.goto(random.randint(-400, 570), random.randint(100, 350))
    s.down()
    s.dot(5, "#757196")


def himmel3():
    s.up()
    s.goto(random.randint(-400, 570), random.randint(100, 350))
    s.down()
    s.dot(5, "#CED5FF")


def himmel4():
    s.up()
    s.goto(random.randint(-400, 570), random.randint(100, 350))
    s.down()


def stern():
    links = 144
    vorne = 12
    s.color("yellow")
    s.begin_fill()
    for x in range(1):
        s.begin_fill()
        s.up()
        s.goto(random.randint(-400, 570), random.randint(100, 350))
        s.down()
        for x in range(5):
            s.forward(vorne)
            s.left(links)
        s.end_fill()


for x in range(17):
    himmel1()
    himmel3()
    himmel2()
    himmel3()

for i in range(10):
    stern()