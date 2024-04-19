import random

words = open('wordlist2.txt').read().splitlines()
generated_word = random.choice(words)
word_check = []
correct_letters = ['.', '.', '.', '.', '.']


def word_to_list(generated_word):
    for letter in generated_word:
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
    wrong_pos = []
    i = 0

    if guess == generated_word:
        return print("That's correct.")

    while i < len(generated_word):
        if generated_word[i] == guess[i]:
            empty_word[i] = guess[i]
            correct_letters[i] = guess[i]

        elif guess[i] in generated_word and generated_word.count(guess[i]) >= guess.count(guess[i]):
            wrong_pos.append(guess[i])
        else:
            print(f"{guess[i]} is niet in het woord")
        i += 1

    print(empty_word, wrong_pos)
    print(correct_letters)
    get_user_input()

print(generated_word)
get_user_input()
