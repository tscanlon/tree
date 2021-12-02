import turtle

s = turtle.getscreen()

t = turtle.Turtle()

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

# So we have a stump now and we'd like to draw some branches

s.exitonclick()
