import time, turtle, random
from utils import *
# Section 1: Setup
set_background("castle")
s1 = create_sprite("character1",0,-200)

# Section 2: define controls
def move_up():
    x = s1.xcor()
    y = s1.ycor() + 10
    s1.goto(x,y)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor() - 15
    s1.goto(x,y)
    
def move_left():
    x = s1.xcor() - 19
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right(): 
    x = s1.xcor() + 24
    y = s1.ycor() 
    s1.goto(x,y)

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_right, "d")
window.onkeypress(move_left, "a")

# Section 3: define other controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")

def draw():
    s1.pendown()

window.onkeypress(draw, "c")

def stop_drawing():
    s1 .penup()


window. onkeypress(stop_drawing, "x")

def erase():
    s1.clear()

window.onkeypress(erase, "1")

def red_pen():
    s1.color("red")

window.onkeypress(red_pen,"2")

def green_pen():
    s1.color ("green")

window.onkeypress(green_pen, "3")

def reset():
    s1.goto (0,0)

window.onkeypress(reset,"r")




s2 = create_sprite("basketball",0,-200)

def move_up():
    x = s1.xcor()
    y = s1.ycor() + 25
    s1.goto(x,y)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor() - 15
    s1.goto(x,y)
    
def move_left():
    x = s1.xcor() - 19
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right(): 
    x = s1.xcor() + 24
    y = s1.ycor() 
    s1.goto(x,y)

window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_right, "Right")
window.onkeypress(move_left, "Left")


def hide():
    s2.hidebasketball()
def show():
    s2.showbasketball()

window.onkeypress(hide, "7")
window.onkeypress(show, "7")






# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()
