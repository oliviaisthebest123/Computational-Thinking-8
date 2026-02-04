import turtle, time, random
from utils import *

# Section 1 - setup
# TODO - set a background using set_background()
set_background( "underwater" )

# TODO - create at least two variables and set their starting value. ex: cookies = 0

fish = 0 
turtle = 0


# OPTIONAL: use this invisible alien to say a message
# message_sprite = create_sprite("alien", -200,200)
# message_sprite.hideturtle()



# Section 2 - controls
# TODO - define an action. ex: def my_control()

def make_fish ():
    global fish
    fish += 1 
    x = random.randint (-200,200)
    y = random.randint (-200,200)
    create_sprite("fish",x,y)
window.onkeypress(make_fish,"space")
#adds fish on the screen when you press space 
def make_turtle ():
    global turtle 
    turtle += 1
    x = random.randint (-200,200)
    y = random.randint (-200,200)
    create_sprite("turtle",x,y)
window.onkeypress(make_turtle,"t")
#adds turtle on screen when you press t 



# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    # message_sprite.clear()
    # message_sprite.write("Hello")

    time.sleep(0.01)
    window.update()
    # goal of the game is to create as many fish and turtles as you can 