# Write a program to standardise user’s name

input_name = input("Please input your name")

# Pre-lowercase list
list_1 = input_name.split()
length = len(list_1)

# After-lowercase list
list_2 = []

# Final list with proper case
list_3 = []

# lowercase characters
for i in range(0,length):
    list_2.append(list_1[i].lower())
    list_3.append(list_2[i].title())
    name = str.join(" ",list_3)

print("Name after conversion: ", name)
