import random
words = open('wordlist2.txt').read().splitlines()
chosen_word = random.choice(words)
word_check = []

def word_to_list(chosen_word):
    for letter in chosen_word:
        word_check.append(letter)

def