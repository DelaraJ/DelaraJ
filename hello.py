import math
from pyexpat.model import XML_CQUANT_NONE
import turtle


x0=-200
y0=200
boxlen=400
x1=x0+boxlen
y1=y0
x2=x1
y2=y0+boxlen
x3=x0y3=y2
xo=0
yo=0
theta=math.pi/6
v0=5
def draw_box(x0,x1,x2,x3,y0,y1,y2,y3)
    turtle.penup()
    turtle.shape('circle')
    turtle.shapesize(4)
    turtle.setpos(x0,y0)
    turtle.pendown()
    turtle.setpos(x1,y1)
    turtle.setpos(x2,y2)
    turtle.setpos(x3,y3)
    turtle.setpos(x0,y0)
def init_game():
    def draw_box(x0,x1,x2,x3,y0,y1,y2,y3)
    turtle.penup()
    turtle.setpos()
init_game()
dx=v0*math.cos(theta)
dy=v0*math.sin(theta)
x=xo
y=yo
def hit-vwall(xb,yb,left_wall,right_wall):
    return xb<=left_wall or xb>=right_wall
def hit-hwall(xb,yb,upperwall_wall,lower_wall):
    return yb<=lower_wall or yb>=upper_wall

while True:
    x=x+dx
    y=y+dy
    if hit_hwall(x,y0,y3):
        dy=-dy
    if hit_vwall(y,x0,x1):
        dx=-dx



