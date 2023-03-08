"""
CS50. Problem Set 2. camelCase.

In a file called camel.py, implement a program that prompts the user
for the name of a variable in camel case and outputs the corresponding
name in snake case. Assume that the user’s input will indeed be in camel case.
"""


def main():
    """
    camel to snake
    """
    name = input("Please write something in camelcase: ")
    convert_camel_to_snake(name)


def convert_camel_to_snake(camelcase):
    """
    camel to snake
    """
    for letter in camelcase:
        if letter.isupper():
            print("_", letter.lower(), end="", sep="")
        else:
            print(letter, end="")
    print("\r")


main()
