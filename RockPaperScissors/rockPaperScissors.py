import random

game_items = ["rock", "paper", "scissors"]
print("Welcome to a game of rock paper scissors")
print("First to 3 points wins the game")

computer_points = 0
user_points = 0

while user_points != 3 and computer_points != 3:
    computer_input = random.choice(game_items)
    user_input = input("\nEnter your choice from \"rock\", \"paper\", and \"scissors\" : ")
    if (user_input.lower() == "rock" and computer_input == "paper") or (user_input.lower() == "paper" and computer_input == "scissors") or (user_input.lower() == "scissors" and computer_input =="rock"):
        computer_points +=1
        print("Rock Paper Scissors Shoot!!!! \nYou: " + user_input + "        Computer: " + computer_input)
        print("\nComputer won that round\n")
        print("Scores:      \nYou: " + str(user_points) + "             Computer: " + str(computer_points))
    elif (user_input.lower() == "paper" and computer_input == "rock") or (user_input.lower() == "scissors" and computer_input == "paper") or (user_input.lower() == "rock" and computer_input =="scissors"):
        user_points +=1
        print("Rock Paper Scissors Shoot!!!! \nYou: " + user_input + "        Computer: " + computer_input)
        print("\nYou won that round\n")
        print("Scores:      \nYou: " + str(user_points) + "             Computer: " + str(computer_points))
    else:
        print("Rock Paper Scissors Shoot!!!! \nYou: " + user_input + "        Computer: " + computer_input)
        print("\nIts a tie\n")
        print("Scores:      \nYou: " + str(user_points) + "             Computer: " + str(computer_points))
        
if computer_points == 3:
    print("\nComputer won the game")
else:
    print("\nYou won the game")
