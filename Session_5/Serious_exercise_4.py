Rabbit_list = [0 , 1]

for i in range(5):
    length = len(Rabbit_list)
    Rabbit_number = Rabbit_list[length - 2] + Rabbit_list[length - 1]
    Rabbit_list.append(Rabbit_number)
  
    new_length = len(Rabbit_list)

    print("Month {0}: {1} pairs of rabbits".format(i,Rabbit_list[new_length - 1]))
  
  





