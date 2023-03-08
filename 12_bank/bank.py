"""
CS50. Problem Set 1. Home Federal Savings Bank.

In a file called bank.py, implement a program that prompts the user
for a greeting.
If the greeting starts with “hello”, output $0. If the greeting starts
with an “h” (but not “hello”), output $20.
Otherwise, output $100.
Ignore any leading whitespace in the user’s greeting,
and treat the user’s greeting case-insensitively.
"""


def main():
    """
    hands out money according to the greeting
    """
    user_greeting = input("Greeting: ")
    print(value(user_greeting))


def value(greeting):
    """
    get the value of the money to pay
    """
    greeting = greeting.lower().lstrip()
    if greeting.startswith("hello"):
        return "$0"
    if greeting.startswith("h"):
        return "$20"
    return "$100"


if __name__ == "__main__":
    main()
