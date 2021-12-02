# Do some pyton ~magic~
import turtle

s = turtle.getscreen()

t = turtle.Turtle()

# Move the turtle (pen) around
t.forward(90)
# Change the pen direction
t.right(90)
t.forward(90)

# Lift the turtle (pen) up
t.up()
# Tell it to go to a specific place
t.goto(0,0)
# Put the pen down
t.down()
# Draw a line to a specific place
t.goto(-100,-100)

# Get a second pen to move around independently
u = t.clone()
u.color("red")
u.goto(100,-100)
t.goto(100,-200)

# ask the turtle where it is
print(u.pos())
print(t.pos())
# pos returns a tumple of the x,y position.

# Wait for you to click before closing the window you drew in
s.exitonclick()
