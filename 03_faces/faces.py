"""
CS50. Problem Set 0. Playback.

In a file called faces.py, implement a function called
convert that accepts a str as input and returns that same
input with any :) converted to 🙂 (otherwise known as a slightly smiling face)
and any :( converted to 🙁 (otherwise known as a slightly frowning face).
All other text should be returned unchanged.
"""


def main():
    """
    Getting user input
    """
    user_text = input()
    print(convert(user_text))


def convert(text):
    """
    Replacing text with emojies
    """
    return text.replace(":)", "🙂").replace(":(", "🙁")


main()
