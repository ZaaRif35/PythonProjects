import turtle

wn = turtle.Screen()
wn.bgcolor("Light green")
wn.title("Turtle")
skk = turtle.Turtle()
skk.color("Blue")

def sqrfunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(90)
        size = size + 5
sqrfunc(6)
sqrfunc(26)
sqrfunc(46)
sqrfunc(66)
sqrfunc(86)
sqrfunc(106)
sqrfunc(126)
sqrfunc(146)
sqrfunc(166)
sqrfunc(186)
sqrfunc(206)
sqrfunc(226)
sqrfunc(246)
sqrfunc(266)

turtle.exitonclick()