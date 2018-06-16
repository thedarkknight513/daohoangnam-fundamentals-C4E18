from turtle import *
from random import randint

def draw_star(x,y,length):
  
    color("white")
    
    goto(x,y)
    color("black")

    for i in range(5):
        forward(length)
        right(144)


speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

mainloop()

