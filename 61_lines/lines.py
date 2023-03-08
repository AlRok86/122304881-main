"""
CS50. Problem Set 6. Lines of Code

in a file called lines.py, implement a program that expects exactly
one command-line argument, the name (or path) of a Python file,
and outputs the number of lines of code in that file, excluding
comments and blank lines.

If the user does not specify exactly one command-line argument, or if
the specified file’s name does not end in .py, or if the specified
file does not exist, the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace,
is a comment. (A docstring should not be considered a comment.) Assume that
any line that only contains whitespace is blank.
"""

import sys


def main():
    """
    main checks the arguments and prints out the number of lines
    """
    check_commandline_argument(sys.argv)
    print(count_lines(sys.argv[1]))


def check_commandline_argument(arguments):
    """
    checks specified command line arguments
    """
    if len(arguments) < 2:
        sys.exit("Too few command-line arguments")
    if len(arguments) > 2:
        sys.exit("Too many command-line arguments")
    if arguments[1][-3:] != ".py":
        sys.exit("Not a Python file")
    try:
        with open(arguments[1], "r", encoding="utf-8"):
            pass
    except FileExistsError:
        sys.exit("File does not exist")


def count_lines(filename):
    """
    counts lines in a file except comments and blanks
    """
    counter = 0
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if line.lstrip().startswith("#"):
                continue
            if line.strip() == "":
                continue
            counter += 1
    return counter


if __name__ == "__main__":
    main()
