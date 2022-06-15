import random

computer_gen_num = random.randrange(1,5,1)
num_tries = 0
correct_guess = False

print(computer_gen_num)

while not(correct_guess) and (num_tries <= 4):
    user_input = input("Enter your guess: ")

    if float(user_input) == computer_gen_num:
        print("You guessed correctly, the number was: " + str(computer_gen_num))
        correct_guess = True
    else:
        num_tries +=1
        print("Your guess is wrong, you have " + str(5 - num_tries) + " more tries")



