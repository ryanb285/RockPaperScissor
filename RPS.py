# RPS.py

import random

print("Rock, Paper, Scissors, Shoot!")

user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")

print(user_choice)

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("Good choice!")
else:
    print("Game canceled")



valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("Computer choice: ", computer_choice)

#this is probably the least useful way possible but hey! it works. 

if(user_choice == "rock") and (computer_choice == "rock") :
    print("tie")

if(user_choice == "rock") and (computer_choice == "paper"):
    print("Computer wins!")

if(user_choice == "rock") and (computer_choice == "scissors"):
    print("User Wins!")

if(user_choice == "paper") and (computer_choice == "rock"):
    print("User Wins!")


if(user_choice == "paper") and (computer_choice == "paper"):
    print("tie")

if(user_choice == "paper") and (computer_choice == "scissors"):
    print("Computer wins!")

if(user_choice == "scissors") and (computer_choice == "rock"):
    print("Computer wins!")


if(user_choice == "scissors") and (computer_choice == "scissors"):
    print("tie")

if(user_choice == "scissors") and (computer_choice == "paper"):
    print("User Wins!")

print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN")

exit()

    
    



