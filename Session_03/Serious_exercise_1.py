Our_items = ["T-shirts","Sweaters"]

# R
print("Our items: ", *Our_items,sep=" ")

# C
new_item =input("Please input new item")
Our_items.append(new_item)
print("Our items ",*Our_items, sep=" ")

# U
replace_position =int(input("Please input the position to be replaced"))
replace_item = input("What do you want to replace?")
Our_items[replace_position-1] = replace_item
print("Our items ",*Our_items,sep=" ")

#D
delete_position=int(input("Please input the position to delete"))
del Our_items[delete_position-1]
print("Our items ",*Our_items,sep=" ")

