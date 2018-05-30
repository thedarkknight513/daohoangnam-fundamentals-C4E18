from random import randint

possible_words =["champion", "meticulous", "hexagon"]

# choose the answer from the list
number_of_possible_answers = len(possible_words)
# print(number_of_possible_answers)
answer_number = randint(0,number_of_possible_answers-1)
correct_word = possible_words[answer_number]
word_list = list(correct_word)
# 



loop_1 = True
count = 1
while loop_1:
    if count <= len(correct_word):
        length = len(word_list)
        random_number = randint(0,length)
        # print(random_number)
        removed_character = word_list[random_number-1]
        del word_list[random_number-1]
        print(removed_character, end=" ")
    else:
        loop_1 = False
    count += 1
print()


loop_2 = True
while loop_2:
    guest_word = input("Please input your guess word")
    if guest_word == correct_word:
        print("Bingo")
        break
    else:
        print("Try again")