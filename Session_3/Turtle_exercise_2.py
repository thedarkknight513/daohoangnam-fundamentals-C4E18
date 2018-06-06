# create list of colors
colors =["red","blue","brown","yellow","grey"]

# specify length
width_lenth = int(input("Please inpput width length"))
height_length = int(input("Please input heigth length"))

# import turtle
from turtle import*
speed(-1)

# draw turtle
for i in range(0,5):
    color(colors[i])
    fillcolor(colors[i])
    begin_fill()

    for j in range(2):
        forward(width_lenth)
        left(90)
        forward(height_length)
        left(90)
    forward(width_lenth)

    end_fill()


mainloop()
