# Write a program to ask user to enter their balance then standardise it

number = int(input("Please input number"))
print(number)

formatted_number = "{:,}".format(number)
print("Your updated balance: $ ",formatted_number)