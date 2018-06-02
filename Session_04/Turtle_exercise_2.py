from turtle import*
color("blue")
speed(-1)

length = int(input("Please input length"))
repeat_times = int(input("Please input the number of repeated times"))

# drawing
left(135)

for j in range(repeat_times):
    for i in range(4):
        forward(length)
        left(90)
    right(360/repeat_times)
    length -= 10
    
mainloop()


