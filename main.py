import random

words = open('wordlist2.txt').read().splitlines()
# chosen_word = random.choice(words)
chosen_word = 'raden'
word_check = []


def word_to_list(chosen_word):
    for letter in chosen_word:
        word_check.append(letter)


def get_user_input():
    user_input = input("Enter your word: ")
    if user_input not in words:
        print("That's not a valid word, retry.")
        return get_user_input()
    else:
        check_user_input(user_input)


def check_user_input(user_input):
    if user_input == chosen_word:
        return print("That's correct.")

    i = 0
    while i < len(chosen_word):
        if chosen_word[i] == user_input[i]:
            print(f"{user_input[i]} is in de juiste positie!")

        elif chosen_word[i] in chosen_word:
            print(f"{user_input[i]} is in het woord, maar niet de juiste positie!")

        else:
            print(f"{user_input[i]} is niet in het woord")
        i += 1


print(chosen_word)
get_user_input()
