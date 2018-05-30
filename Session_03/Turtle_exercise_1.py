# List down colors
colors =["red","blue","brown","yellow","grey"]

# Define length
length = int(input("Please input length"))

# Draw turtle
from turtle import*
speed(-1)


for i in range(3,8):
    for j in range(i):
        color(colors[i-3])
        forward(length)
        left(360/i)


mainloop()
