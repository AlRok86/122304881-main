"""
CS50. Problem Set 2. Just setting up my twttr.

In a file called twttr.py, implement a program that prompts
the user for a str of text and then outputs that same text
but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase.
"""


def main():
    """
    omits all vowels
    """
    word = input("Input: ")
    for letter in word:
        if letter.upper() not in ('A', 'E', 'O', 'U', 'I'):
            print(letter, end="")
    print("\r")


if __name__ == "__main__":
    main()
