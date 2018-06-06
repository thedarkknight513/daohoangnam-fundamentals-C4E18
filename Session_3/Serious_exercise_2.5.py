# 2.5 Let do this for 4 months (or as long as you want):

flock_size =[5, 7, 300, 90, 24, 50, 75]
highest = max(flock_size)

print("Hi, my name is Nam and this is my sheep size:")
print(*flock_size, sep =", ")

month = int(input("Please input the number of months"))


for i in range(1,month+1):
    for j in range(0,7):
        flock_size[j] += 50

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
