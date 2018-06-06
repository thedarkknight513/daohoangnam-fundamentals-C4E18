# Bacteria B replicates itself each 2 minutes, write a program that asks users to enter two numbers: the initial B 
# bacteria number and a period of time (in minutes). Calculate and print out the total number of B bacteria after this period.

initial_bacteria = int(input("Please input the initial number of bacteria"))
period_of_time = int(input("Please input the period of time in minutes"))

number_of_bacteria_after = int(initial_bacteria * (2 ** (period_of_time / 2)))
# print(number_of_bacteria_after)
print("After {0} minutes we would have {1} bacteria".format(period_of_time, number_of_bacteria_after))