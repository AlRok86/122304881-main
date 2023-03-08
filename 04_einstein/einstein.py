"""
CS50. Problem Set 0. Einstein.

In a file called einstein.py, implement a program in Python
that prompts the user for mass as an integer (in kilograms)
and then outputs the equivalent number of Joules as an integer.
Assume that the user will input an integer.
"""


def main():
    """
    converting kg to J
    """
    kilograms = int(input())
    print(convert_kilo_to_joules(kilograms))


def convert_kilo_to_joules(kilos):
    """
    calculating Joules
    """
    speed_of_light = 3 * (10 ** 8)
    return kilos * (speed_of_light ** 2)


main()
