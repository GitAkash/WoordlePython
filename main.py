import random

words = open('wordlist2.txt').read().splitlines()
generated_word = random.choice(words)
word_check = []
correct_letters = ['.', '.', '.', '.', '.']
wrong_letters = set()

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
            wrong_letters.add(guess[i])
        i += 1

    print(f"Goede Letters (Ronde): \t \t \t Verkeerde Positie:")
    print(f" {empty_word} \t\t  {wrong_pos}")
    print(f"Goede Letters (Totaal): \t \t Foute Letters (Totaal):")
    print(f" {correct_letters} \t\t  {wrong_letters}")
    get_user_input()

get_user_input()
