# adventure_game.py - Jeff Hritz
# Currently still in development

"""
Text-based adventure game.
"""

import time


def intro():
    """Intro sequence."""
    print("\n" * 100)
    print("You are asleep, but still aware.")
    time.sleep(2)
    print("The world is a blur around you.")
    time.sleep(2)
    print("You feel yourself moving.")
    time.sleep(2)
    print("Floating")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("Wake up.")
    time.sleep(3)
    print("\n" * 100)
    time.sleep(4)
    print("You wake up in a forest in the early morning.")
    time.sleep(2)
    print("You don't know where you are.")
    time.sleep(2)
    print("This forest feels strange.")
    time.sleep(2)
    start()


def choose():
    print("Choose")
    choice = input()
    return choice


def start():
    """Starting area. Provides user the first choice."""

    print("What do you do?")
    time.sleep(2)

    def starting_choice():
        cmd = choose()
        if cmd == "1":
            print("You take a big poopy shit.")
            start()
        elif cmd == "2":
            print("You hold your breath until you become an hero.")
        elif cmd == "3":
            print("You walk deeper into the woods.")
            a = input()
        elif cmd == "4":
            print("You scream at the top of your lungs.\n"
                  "The sound of your voice echoing into the quiet woods frightens you")
            start()
        elif cmd == "5":
            print("5")
        else:
            print("Choose again.")
            starting_choice()

    print("----------")
    print("1. poop\n"
          "2. kill yourself\n"
          "3. walk into the woods\n"
          "4. scream\n"
          "5. stay put\n")
    starting_choice()


# def getcmd(cmdlist):
#     """Choice router based on user input and available options in each scenario."""
#     if cmd in cmdlist:
#         return cmd


if __name__ == "__main__":
    start()
