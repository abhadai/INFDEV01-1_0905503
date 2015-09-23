import random

# The choices in the game
choices = ["rock", "paper", "scissors"]

# Ask the users for their choice
player_one_choice = input("Player 1, type rock, paper or scissors\n\r")

# If choice exists, continue game
if(player_one_choice in choices):
    print("CHOICE FOUND" + player_one_choice)

    # Rock and rock ties
    if(player_one_choice == "rock" and player_two_choice == "rock"):
        print("No one wins!")

    # Paper beats rock
    if(player_one_choice == "rock" and player_two_choice == "paper"):
        print("P2 wins!")
    
    # Rock beats scissors      
    if(player_one_choice == "rock" and player_two_choice == "scissors"):
        print("P1 wins")
    
    # Paper beats rock
    if(player_one_choice == "paper" and player_two_choice == "rock"):
        print("P1 wins!")

    if(player_one_choice == "paper" and player_two_choice == "paper"):
        print("P2 wins!")

    if(player_one_choice == "paper" and player_two_choice == "scissors"):
        print("P1 wins")

else:
    # If choice doesn't exist, ask again
    player_one_choice = input("Player 1 your choice was not found, type rock, paper or scissors\n\r")

# If choice exists, continue game
if(player_one_choice in choices):
    print("CHOICE FOUND" + player_one_choice)
else:
    # If choice doesn't exist, ask again
    player_two_choice = input("Player 2 your choice was not found, type rock, paper or scissors\n\r")