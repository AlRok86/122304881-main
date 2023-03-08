"""
CS50. Problem Set 2. Just setting up my twttr.

In a file called twttr.py, implement a program that prompts
the user for a str of text and then outputs that same text
but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase.
"""
def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    shortened_word = ""
    for letter in word:
        if (letter.upper() != 'A'
        and letter.upper() != 'E'
        and letter.upper() != 'O'
        and letter.upper() != 'U'
        and letter.upper() != 'I'
        ):
            shortened_word += letter
    return shortened_word

if __name__ == "__main__":
    main()