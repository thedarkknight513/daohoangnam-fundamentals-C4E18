from turtle import*
color("blue")
speed(-1)

repeat_times = int(input("Please input the number of shapes"))
length = int(input("Please input length"))

# drawing
for j in range(repeat_times):
    left(360/repeat_times)
    for i in range(4):
        forward(length)
        left(90)

mainloop()
