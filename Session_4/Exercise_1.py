list_1 = [1, 10, 6, 5, 3, 4, 2, 9, 7, 8]
length = len(list_1)

for i in range(0,length -1):
    for j in range(0,length - 1 - i):
        if list_1[j] > list_1[j+1]:
            list_1[j], list_1[j+1] = list_1[j+1], list_1[j]

print("After sorted, the list is : ",list_1)