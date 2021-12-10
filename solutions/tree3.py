import turtle

s = turtle.getscreen()

t = turtle.Turtle()

l = turtle.Turtle()
r = l.clone()
l.color("cyan")
r.color("magenta")
# all together now in a function
def draw_stump(half_width, height):
    r.goto(half_width,0)
    r.goto(half_width,height)
    l.goto(-1*half_width,0)
    l.goto(-1*half_width,height)

def draw_branch(overhang, drop, height, recess):
    """Draws a branch with 4 required variables:
    overhang: how far out from the center of the tree
    drop: how far to drop as you go out
    height: how far up from the starting point to draw
    recess: how far towards the center from the starting point to end the branch
    """
    lstart = l.pos()
    rstart = r.pos()
    r.goto(rstart[0]+overhang, rstart[1]-drop)
    l.goto(lstart[0]-overhang, lstart[1]-drop)
    r.goto(rstart[0]-recess, rstart[1]+height)
    l.goto(lstart[0]+recess, lstart[1]+height)

draw_stump(20,100)

draw_branch(50,10,50,10)


# So we have a stump now and we'd like to draw some branches

s.exitonclick()
