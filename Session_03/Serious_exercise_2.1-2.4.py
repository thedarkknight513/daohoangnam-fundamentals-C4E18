# 2.1 Create a list to represent the sizes of your flock, using list, and print all of your flock size

flock_size =[5, 7, 300, 90, 24, 50, 75]
highest = max(flock_size)

print("Hi, my name is Nam and this is my sheep size:")
print(*flock_size, sep =", ")
print("*"* 20)
#------------------------------------------------------------------------------

# 2.2 At the end of each month, you have to choose one and only one sheep to shear and thus you want to choose 
# the biggest one to maximize your profit. Write a program to search for the biggest sheep in your list:

biggest_sheep = max(flock_size)
print("Now my biggest sheep has size ", biggest_sheep," let's shear it" )
n = flock_size.index(biggest_sheep)
print("*"* 20)

#------------------------------------------------------------------------------

# 2.3 When your biggest sheer, its size will return to the default size, which is 8. 
# Print out your ship size after shearing the biggest one

biggest_sheep_location = flock_size.index(biggest_sheep)
flock_size[biggest_sheep_location] = 8
print("After shearing, now here is my flock")
print(*flock_size, sep = ", ")

print("*"* 20)
#-------------------------------------------------------------------------------

# 2.4 In the following month, EVERY sheep in your flock grow, they have their size increased by 50. Print them out 

for i in range(0,7):
    flock_size[i] += 50
print("One month passed, now here is my flock")
print(*flock_size, end=", ")

print("*"* 20)
#--------------------------------------------------------------------------------










# 