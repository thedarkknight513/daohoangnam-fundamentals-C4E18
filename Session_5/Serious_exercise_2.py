# Write a program to count number occurrences in a list, with AND without using count() function


number =[1, 6, 8, 1, 2, 1, 5, 6]
length = len(number)

number_to_count = int(input("Enter a number"))

loop = True
count = 0

while True:
    for i in range(length):
        if number[i] == number_to_count:
            count += 1
    break
print("{0} appears {1} times in my list".format(number_to_count,count))