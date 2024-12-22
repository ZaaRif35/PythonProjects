import  turtle
colors = ["red", "green", "blue", "purple", "orange", "yellow"]
t = turtle.Pen()
t.bgcolor("Black")
for x in range(360):
    t.pencolor(colors[x%])