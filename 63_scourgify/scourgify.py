"""
CS50. Problem Set 6. Scourgify

In a file called scourgify.py, implement a program that:

Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input,
whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should
be, in order, first, last, and house.

Converts that input to that output, splitting each name into a
first name and last name. Assume that each student will have
both a first name and last name.
If the user does not provide exactly two command-line arguments,
or if the first cannot be read, the program should exit via
sys.exit with an error message.
"""
import sys
import csv


def main():
    """
    reads csv, ouptputs csv
    """
    check_commandline_argument(sys.argv)
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    write_file_in_different_format(input_filename, output_filename)


def check_commandline_argument(arguments):
    """
    checks specified command line arguments
    """
    if len(arguments) < 3:
        sys.exit("Too few command-line arguments")
    if len(arguments) > 3:
        sys.exit("Too many command-line arguments")
    if arguments[1][-4:] != ".csv":
        sys.exit("Not a CSV file")
    try:
        with open(arguments[1], "r", encoding="utf-8"):
            pass
    except FileExistsError:
        sys.exit("File does not exist")


def write_file_in_different_format(input_filename, output_filename):
    """
    reads one file, changes format and writes another file
    """
    with open(input_filename, "r", encoding="utf-8") as read_file:
        reader = csv.DictReader(read_file)
        with open(output_filename, "w", encoding="utf-8") as write_file:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(write_file, fieldnames)
            writer.writeheader()
            for row in reader:
                names = row["name"].split(",")
                first = names[1].strip()
                last = names[0]
                newrow = {"first": first, "last": last, "house": row["house"]}
                writer.writerow(newrow)


if __name__ == "__main__":
    main()
