# pig_latin.py - Jeff Hritz
"""
Generates a pig-latinized version of a user inputted string.
"""

# Only works with 90% of words. Sometimes it outputs slightly in-correct pig latin.


def pig_latin():
    string = input("Enter a word to pig-latinize: ")
    first = string[:1]
    print(string[1:] + '-' + first + 'ay')
    do_another()


def do_another():
    another = input('\nDo another? Yes or no:')
    if another in ['YES', 'Yes', 'yes', 'Y', 'y']:
        pig_latin()
    elif another in ['NO', 'No', 'no', 'N', 'n']:
        quit()
    else:
        print("Incorrect entry, try again: ")
        do_another()


pig_latin()
