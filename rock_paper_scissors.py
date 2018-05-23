# rock_paper_scissors.py - Jeff Hritz
"""
A simple rock, paper, scissors game between the user and a computer.
"""

from random import randint

# Possible actions (All upper'ed to eliminate user mis-types in below function.
draw = ["ROCK", "PAPER", "SCISSORS"]


def computer_choice():
    # Computer makes their move at random.
    computer = draw[randint(0, 2)]
    return computer


def player_choice():
    # Player makes their move
    print("Rock, Paper, or Scissors?")
    player = input("Enter your choice: ")
    return player


def decide_winner():
    # Logic to determine who wins
    player = player_choice().upper()
    computer = computer_choice().upper()
    print("----------------")
    print("Player - " + player)
    print("Computer - " + computer)
    if player == computer:
        print("It's a tie!")
    elif player == "ROCK":
        if computer == "PAPER":
            print("Computer wins!")
        elif computer == "SCISSORS":
            print("Player wins!")
    elif player == "PAPER":
        if computer == "ROCK":
            print("Player wins!")
        elif computer == "SCISSORS":
            print("Computer wins!")
    elif player == "SCISSORS":
        if computer == "ROCK":
            print("Computer wins!")
        elif computer == "PAPER":
            print("Player wins!")
    else:
        print("You've chosen incorrectly, try again.")
        decide_winner()
    a = input("Press any key to play again: ")
    decide_winner()


if __name__ == "__main__":
    decide_winner()
