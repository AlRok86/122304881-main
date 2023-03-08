"""
CS50. Problem Set 4. Little Professor

In a file called professor.py, implement a program that:

Prompts the user for a level,
. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = ,
wherein each of X and Y is a non-negative integer with n digits.
No need to support operations other than addition (+).

Prompts the user to solve each of those problem. If an answer is not correct
(or not even a number), the program should output EEE and prompt the user
again, allowing the user up to three tries in total.
If the user has still not answered correctly after
three tries, the program should output the correct answer.
The program should ultimately output the user’s score, a number out of 10.
"""

import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        int_a = generate_integer(level)
        int_b = generate_integer(level)
        task = str(int_a) + " + " + str(int_b) + " = "
        for i in range(3):
            try:
                solution = int(input(task))
                if solution != int_a + int_b:
                    raise ValueError
                score += 1
                break
            except ValueError:
                if i == 2:
                    print(str(int_a + int_b))
                else:
                    print("EEE")
                continue
    print("Score: ", score)


def get_level():
    while True:
        try:
            level = int(input("Level:"))
            if level not in [1, 2, 3]:
                raise ValueError
            break
        except ValueError:
            continue
    return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 10)
    else:
        return random.randint(10**(level-1), 10**level)


if __name__ == "__main__":
    main()
