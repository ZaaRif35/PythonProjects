import turtle

polygon = turtle.Turtle()
num.sides = 6
side_legth = 70
angle = 360 / num_sides

for i in range(num_sides):
    polygon.forward(side_legth)
    polygon.right(angle)

turtle.exitonclick()