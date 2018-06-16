# Write a function named is_inside that checks if a point is inside a rectangle, takes 2 parameters,
#  the first is a list with 2 elements respectively represents x and y coordinates of the given point, 
#  the second is a list with 4 elements respectively represents x, y coordinates and width height of the given rectangle

def is_inside(coordinate_point_x, coordinate_point_y,coordinate_rectangle_x, coordinate_rectangle_y, rectangle_width, rectangle_height): # this is the
    rectangle_range_of_width = [coordinate_rectangle_x, coordinate_rectangle_x + rectangle_width]
    rectangle_range_of_height = [coordinate_rectangle_y, coordinate_rectangle_y + rectangle_height]

    is_inside_or_not = True

    if rectangle_range_of_width[0] <= coordinate_point_x and rectangle_range_of_width[1] >= coordinate_point_x:
        if rectangle_range_of_height[0]<= coordinate_point_y and rectangle_range_of_height[1] >= coordinate_point_y:
            is_inside_or_not = True
        else:
            is_inside_or_not = False
    else: 
        is_inside_or_not = False

    return is_inside_or_not


result = is_inside(100,120,140,60,100,200)
if result == True:
    print("Inside")
else:
    print("Outside")

