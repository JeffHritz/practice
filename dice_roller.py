# dice_roller.py - Jeff Hritz

"""
Rolls a six sided dice and displays the result.
This could be edited to include multiple dice and dice with as many sides as needed.
"""

from random import randint


# Possible rolls of the dice
rolls = [1, 2, 3, 4, 5, 6]

# Set roll to False to initiate a non-functioned loop
roll = False
while roll is False:
    input("Press any key to roll the dice")     # Meaningless user input to initiate the random roll.
    roll = rolls[randint(0, 5)]                 # Indexes the rolls list using a random number
    print(roll)                                 # Prints the random choice from the rolls list
    roll = False                                # Sets roll to False to re-start the while loop
