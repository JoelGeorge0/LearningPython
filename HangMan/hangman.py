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


    while len(letters_in_word)>0:
        print("You have used these letters: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in random_word]

        print("current word: ", " ".join(word_list))

        user_letter = input("Enter a string: ").lower()

        if user_letter.lower() in alphabet - used_letters:
            used_letters.add(user_letter.lower())
            if user_letter.lower() in letters_in_word:
                letters_in_word.remove(user_letter.lower())   
        elif user_letter.lower() in used_letters:
            print("The letter has already been guesssed")
        else:
            print("Invalid entry")

    print("congrants you guess correclty, the word was: " + random_word)


hangman()