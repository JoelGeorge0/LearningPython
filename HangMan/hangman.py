from words import words
import random
import string

def get_valid_word(words):
    word = random.choice(words)
    while "-" in words or " " in words:
        word = random.choice(words)
    return word.lower()


def hangman():
    random_word = get_valid_word(words)
    print(random_word)

    letters_in_word = set(random_word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()
    user_letter = input("Enter a string: ")
    print(letters_in_word)

    if user_letter.lower() in alphabet - used_letters:
        print("checking guess")
        used_letters.add(user_letter)
        if user_letter in letters_in_word:
            letters_in_word.remove(user_letter)
            
    elif user_letter.lower() in used_letters:
        print("The letter has already been guesssed")
    else:
        print("Invalid entry")



hangman()