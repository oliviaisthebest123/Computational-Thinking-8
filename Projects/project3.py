import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 =-100
y1 =100
x2 =-100
y2 =50
x3 =-100
y3 =0
x4 =-100
y4 =-50


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("underwater")
t1 = create_sprite("image",x1,y1)
t2 = create_sprite("fish3",x2,y2)
t3 = create_sprite("fish2",x3,y3)
t4 = create_sprite("fish4",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # because they are all random we cannot know which one will win 
for i in range(40):
    x1 += random.randint (1,10)
    x2 += random.randint (1,10)
    x3 += random.randint (1,10)
    x4 += random.randint (1,10)

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)

# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4

winner = max(x1, x2, x3, x4)

if x1 == winner:
    print("player 1 wins!")
if x2 == winner:
    print("player 2 wins!")
if x3 == winner:
    print("player 3 wins!")
if x4 == winner:
    print("player 4 wins!")

turtle.exitonclick()