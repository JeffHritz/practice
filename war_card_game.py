# war_card_game.py - Jeff Hritz
"""
The card game called war. Players each get half of a shuffled deck of 52 cards. Each player draws cards and
the winner is determined by whoever drew the higher value card. If players both draw the same card war begins to break
the stalemate. When a stalemate occurs each player draws three cards and the value of the third card determines the
winner. If the player doesn't have three cards they used their remaining cards and their last card is used to determine
the winner.
The first player to run out of cards loses.
"""

# In development

import random
import time


def generate_deck(suites=4, card_values=13):
    """Generates and shuffles a deck of 52 cards."""
    cards = []
    for suite in range(suites):
        for value in range(1, card_values+1):
            cards.append(value)
    random.shuffle(cards)
    return cards


def play_war(deck):
    """Divides the deck of cards between two players and creates a stash for won cards."""
    player_cards = deck[:len(deck)/2]
    computer_cards = deck[len(deck)/2:]
    player_stash = []
    computer_stash = []
    while player_cards and computer_cards:
        print("lol")


if __name__ == "__main__":
    deck = generate_deck()
    play_war(deck)
