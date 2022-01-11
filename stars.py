# # # # # # # # # # # # # # # # #
#
#   Created by 
#   Abhinav Bhardwaj
#   on 28/12/21  at   11:36 PM
#
# # # # # # # # # # # # # # # # #


import colorsys as csys
import turtle as t

T = t.Turtle()
S = t.Screen()


S.bgcolor('white')
T.speed(5)

T.hideturtle()      # To hide cursor
T.penup()           # To avoid printing the movement of the cursor before printing stars
T.goto(10, 180)     # Putting cursor in the position so that complete fig will be in center
T.pendown()

n = 20
h = 10

print("\nPrinting Coloured Stars ...")

T.left(107)
for i in range(100, 0, -1):
    c = csys.hsv_to_rgb(h, 1, 0.9)
    h += 1/n
    T.color(c)
    T.left(144)
    T.forward(5 * i)

print("\nColoured Stars Printed\n")