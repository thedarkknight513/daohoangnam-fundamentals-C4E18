
# Game: Guess my numbers

from random import randint
correct_number = randint(1,100)
print(correct_number)

loop = True


while loop:
    guessed_number = int(input("Input your guess, a number range from 1-100"))
    if guessed_number == correct_number:
        print("Bingo")
        break
    elif guessed_number < correct_number:
        print("Bigger")
    else:
        print("Smaller")
