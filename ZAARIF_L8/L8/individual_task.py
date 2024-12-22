import turtle
t=turtle.Turtle()
t.penup()

t.speed(1)
t.goto(-30,50)
t.pendown()
t.pensize(5)
t.pencolor("black")
t.right(180)
t.forward(50)
t.left(90)
t.forward(60)
t.left(90)
t.forward(50)
t.left(90)
t.forward(27)
t.left(90)
t.forward(20)
t.pencolor("white")
t.goto(0,0)

turtle.done

turtle.exitonclick()