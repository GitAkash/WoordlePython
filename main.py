import random

words = open('wordlist2.txt').read().splitlines()
chosen_word = random.choice(words)
word_check = []


def word_to_list(chosen_word):
    for letter in chosen_word:
        word_check.append(letter)


def get_user_input():
    guess = input("Enter your word: ")
    if guess not in words:
        print("That's not a valid word, retry.")
        return get_user_input()
    else:
        check_user_input(guess)


def check_user_input(guess):
    empty_word = ['.','.','.','.','.']
    guessed_letters = []
    wrong_pos = []
    i = 0

    if guess == chosen_word:
        return print("That's correct.")

    while i < len(chosen_word):
        if chosen_word[i] == guess[i]:
            # print(f"{guess[i]} is in de juiste positie!")
            empty_word[i] = chosen_word[i]
            guessed_letters.append(chosen_word[i])
        elif guess[i] in chosen_word and chosen_word.count(guess[i]) >= guess.count(guess[i]):
            # print(f"{guess[i]} is in het woord, maar niet de juiste positie!")
            wrong_pos.append(guess[i])
        else:
            print(f"{guess[i]} is niet in het woord")
        i += 1
    print(empty_word, wrong_pos)
    get_user_input()

get_user_input()
