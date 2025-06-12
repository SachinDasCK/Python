#####################################
# Author: Sachin Das	
# Date : 12/06/2025
# Description : Rock Paper Scissors Game
####################################################

import random


def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissors): ")
    computer_choice = random.choice(["rock", "paper", "scissors"])
    choices= {"player": player_choice, "computer": computer_choice}
 
    return choices

def check_win(player,computer):
    print(f"Player chose: {player} and computer chose: {computer}") 
    if player == computer:
        return "It's a tie!"
    elif ((player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper")):
        return "Player wins!"
    else:
        return "Computer wins!"

choices = get_choices()
results = check_win(choices["player"], choices["computer"])
print(results)