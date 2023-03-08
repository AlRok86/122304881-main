"""
CS50. Problem Set 4. Guessing Game

In a file called game.py, implement a program that:

Prompts the user for a level n,

If the user does not input a positive integer, the program should prompt again.

Randomly generates an integer between 1 and n, inclusive,
using the random module.

Prompts the user to guess that integer. If the guess is not a positive integer,
the program should prompt the user again.

If the guess is smaller than that integer,
the program should output Too small! and prompt the user again.

If the guess is larger than that integer,
the program should output Too large! and prompt the user again.

If the guess is the same as that integer,
the program should output Just right! and exit.

"""
import random


def main():
    """
    plays the game
    """
    level = get_positive_integer("Level: ")
    number = random.randint(1, level)
    guess_number(number)


def guess_number(number):
    """
    A loop till you hit the number
    """
    while True:
        guessed_number = get_positive_integer("Guess: ")
        if number < guessed_number:
            print("Too large!")
        elif number > guessed_number:
            print("Too small!")
        else:
            print("Just right!")
            break


def get_positive_integer(prompt):
    """
    asks till a positive integer is given
    """
    while True:
        try:
            level = int(input(prompt))
            if level < 1:
                raise ValueError
            break
        except ValueError:
            continue
    return level


if __name__ == "__main__":
    main()
