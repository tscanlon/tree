import turtle

s = turtle.getscreen()

t = turtle.Turtle()

# Lets focus just on the stump
t.goto(50,0)
t.goto(50,100)
t.up()
t.goto(0,0)
t.down()
t.goto(-50,0)
t.goto(-50,100)
# Where does it feel like we've repeated outselves here?
# Lets add some variables!
# Do we want only one pen to solve this problem?
# Lets try to solve this using two pens.
# What if we want to draw multiple stumps of different sizes?
# Lets turn this into a function!

s.exitonclick()
