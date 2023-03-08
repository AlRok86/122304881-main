"""
CS50. Problem Set 6. Pizza

In a file called pizza.py, implement a program that expects
exactly one command-line argument, the name (or path) of a
CSV file in Pinocchio’s format, and outputs a table formatted
as ASCII art using tabulate, a package on PyPI at
pypi.org/project/tabulate. Format the table using the library’s
grid format. If the user does not specify exactly one command-line
argument, or if the specified file’s name does not end in .csv,
or if the specified file does not exist, the program should instead
exit via sys.exit.
"""
import sys
import csv
from tabulate import tabulate


def main():
    """
    main checks the arguments and prints out the pizza in ASCII
    """
    check_commandline_argument(sys.argv)
    filename = sys.argv[1]
    file_in_tabulate_format(filename)


def check_commandline_argument(arguments):
    """
    checks specified command line arguments
    """
    if len(arguments) < 2:
        sys.exit("Too few command-line arguments")
    if len(arguments) > 2:
        sys.exit("Too many command-line arguments")
    if arguments[1][-4:] != ".csv":
        sys.exit("Not a CSV file")
    try:
        with open(arguments[1], "r", encoding="utf-8"):
            pass
    except FileExistsError:
        sys.exit("File does not exist")


def file_in_tabulate_format(filename):
    """
    turns list of list to tabulate format
    """
    with open(filename, "r", encoding="utf-8") as file:
        table = []
        reader = csv.reader(file)
        for row in reader:
            table.append(row)
        headers = table[0]
        table = table[1:]
        print(tabulate(table, headers, tablefmt="grid"))


if __name__ == "__main__":
    main()
