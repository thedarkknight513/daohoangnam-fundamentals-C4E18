# 9.	Write a function that extracts the even items in a given integer list, named get_even_list, 
# takes 1 parameter: l, where l is the given integer list ([1, 4, 5, -1, 10] for example), returns a new
#  list contains only even numbers ([4, 10] if the given list is [1,4,5,-1,10])

# list_1 = [1, 4, 5, -1, 10] 
def get_even_list(list_1):
    list_2 = []

    for item in list_1:
        if item % 2 == 0:
            list_2.append(item)
    return list_2

even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
    

