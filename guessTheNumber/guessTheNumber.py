import random

computer_gen_num = random.randrange(1,5,1)
num_tries = 0
user_input = 0

while (float(user_input) != computer_gen_num) and (num_tries <= 4):
    user_input = input("Enter your guess (between 1 and 5): ")

    if float(user_input) == computer_gen_num:
        print("You guessed correctly, the number was: " + str(computer_gen_num))
    else:
        num_tries +=1
        print("Your guess is wrong, you have " + str(5 - num_tries) + " more tries")
        if(float(user_input) > computer_gen_num):
            print("The random number is less than " + str(user_input))
        else:
            print("The random number is greater than " + str(user_input))


if float(user_input) != computer_gen_num:
    print("The random number was " + str(computer_gen_num))

