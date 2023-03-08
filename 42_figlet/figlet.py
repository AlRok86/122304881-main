"""
CS50. Problem Set 4. Frank, Ian and Glen’s Letters.

In a file called figlet.py, implement a program that:
Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the
two should be -f or --font, and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font,
the program should exit via sys.exit with an error message.
"""
import pyfiglet
import sys

def main():
    figlet = get_figlet()
    text = input("Write some text: ")
    print(figlet.renderText(text))


def get_figlet():
    if len(sys.argv) not in [1, 3]:
        sys.exit("Invalid usage")
    if len(sys.argv) == 3 and sys.argv[1] not in ['-f', '-font']:
        sys.exit("Invalid usage")
    if len(sys.argv) == 3:
        try:
            figlet = pyfiglet.Figlet(font = sys.argv[2])
        except:
            sys.exit("Invalid usage")
    else:
        figlet = pyfiglet.Figlet(font = 'slant')
    return figlet


if __name__ == "__main__":
    main()