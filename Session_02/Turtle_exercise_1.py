from turtle import*
speed(-1)
color("green")

# Hinh thoi co 2 goc 30' 
x = 100
y = x * (3 ** (0.5))
z = 2 * x

for i in range(2):
    left(30)
    forward(z)
    right(60)
    forward(z)
    left(-120)
    forward(z)
    right(60)
    forward(z)
    forward(z)
    left(60)
    forward(z)
    right(-120)
    forward(z)
    left(60)
    forward(z)
    left(60)

mainloop()