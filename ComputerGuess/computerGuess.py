
import random

def computerGuess(min_range, max_range):

    correct_guess= False
    user_input = "placeHolder"
    print("Think of a number between " + str(min_range) + " and " + str(max_range))

    while user_input.lower() != "yes":
        user_input = input("Enter \"yes\" when ready: ")

    while not(correct_guess):
        computer_guess = random.randint(min_range, max_range)
        print("Is the number your thinking of " + str(computer_guess))
        user_input = input("Is the guess correct? (Enter yes/no): ")

        if user_input.lower() == "yes":
            print("Dont be suprised, its magic")
            correct_guess = True
        elif user_input.lower() == "no":
            user_input = input("Is your number higher or lower? (Enter high/low): ")
            if user_input.lower() == "low":
                max_range = computer_guess - 1
            elif user_input.lower() == "high":
                min_range = computer_guess + 1
            else:
                print("Invalid Entry")
                correct_guess = True
        else:
            print("Invalid Entry")
            correct_guess = True


computerGuess(1, 22)