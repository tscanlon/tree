import turtle

s = turtle.getscreen()


# using more variables
t = turtle.Turtle()
x = 50
y = 100
t.goto(x,0)
t.goto(x,y)
t.up()
t.goto(0,0)
t.down()
t.goto(-1*x,0)
t.goto(-1*x,y)

# Now lets try with two pens
# we can rename them left and right to make it easier to remember later
l = turtle.Turtle()
r = l.clone()
l.color("blue")
r.color("red")
r.goto(50,0)
r.goto(50,100)
l.goto(-50,0)
l.goto(-50,100)


l = turtle.Turtle()
r = l.clone()
l.color("cyan")
r.color("magenta")
# all together now in a function
def draw_stump_all_together_now(half_width, height):
    r.goto(half_width,0)
    r.goto(half_width,height)
    l.goto(-1*half_width,0)
    l.goto(-1*half_width,height)

draw_stump_all_together_now(50,100)

s.exitonclick()
