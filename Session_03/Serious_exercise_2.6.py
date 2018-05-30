# 2.6 After day by day shearing sheep, you became bored. You want to sell your flock to travel the world. In order to have fair trade, 
# you must now calculate the total size of your sheep and then the expected money you can get from your flock before going to the market. 
# Write a program to calculate the total size of your sheep as well as the money you would have

flock_size =[5, 7, 300, 90, 24, 50, 75]
highest = max(flock_size)

print("Hi, my name is Nam and this is my sheep size:")
print(*flock_size, sep =", ")

month = int(input("Please input the number of months"))
biggest_sheep = max(flock_size)
biggest_sheep_location = flock_size.index(biggest_sheep)
flock_size[biggest_sheep_location] = 8

print("Now my biggest sheep has size ", highest," let's shear it")
print("After shearing, here is my flock")
print()
print(*flock_size, end=", ")

for i in range(1,month+1):
    for j in range(0,7):
        flock_size[j] += 50
    print()
    print(i," month have passed, now here is my flock")
    print(*flock_size, end =", ")
    biggest_sheep = max(flock_size)
    biggest_sheep_location = flock_size.index(biggest_sheep)
    print()
    print("Now my biggest sheep has size ",biggest_sheep," let's shear it")
    print("After shearing, here is my flock")
    flock_size[biggest_sheep_location] = 8
    print(*flock_size, sep = ", ")
    print("*" * 20)

# print(*flock_size, end=", ")
flock_total = sum(flock_size)
money_receive = sum(flock_size)* 2
print()
print("My flock has size in total: ",flock_total)
print("I would get ",flock_total,"* 2"," = ",money_receive,"$")
