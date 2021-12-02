import turtle

s = turtle.getscreen()

t= turtle.Turtle()
t.backward(90)
t.right(90)
t.backward(90)
t.right(90)
t.backward(90)
t.left(135)
t.backward(90)
t.left(20)
t.forward(150)
t.right(20)
t.backward(100)
t.left(20)
t.forward(250)
t.right(110)
t.forward(250)
t.right(-20)
t.backward(100)
t.left(-20)
t.forward(150)
t.right(130)
t.forward(150)
# This is where I got after about 15min of guessing not very pretty huh?
# I found guessing angles and lengths to be weird.
# Especially at the end when I wanted to try and connect the start and end of
# the path.
# I find that this method of controling the turtle to be awkward so lets
# scrap this and try something different

s.exitonclick()
