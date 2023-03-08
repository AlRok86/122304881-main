"""
CS50. Problem Set 2. Vanity Plates.

In plates.py, implement a program that prompts the user for a vanity plate
and then output Valid if meets all of the requirements or
Invalid if it does not.
Assume that any letters in the user’s input will be uppercase.
Structure your program per the below, wherein is_valid returns True if s
meets all requirements and False if it does not. Assume that s will be
a str.
You’re welcome to implement additional functions for is_valid to call
(e.g., one function per requirement).

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers)
and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end.
For example, AAA222 would be an acceptable … vanity plate; AAA22A would not
be acceptable.
The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”

"""


def main():
    """
    prints if the plate valid
    """
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate_name):
    """
    checks if the plate valid
    """
    return is_starting_2letter(plate_name) \
        and is_containing_6chars(plate_name) \
        and is_numbers_at_the_end(plate_name) \
        and is_only_chars_numbers(plate_name)


def is_starting_2letter(plate):
    """
    the plate should start with 2 alphanumeric chars
    """
    return plate[0:2].isalpha()


def is_containing_6chars(plate):
    """
    the plate can contain 2 to 6 chars
    """
    number_of_chars = 0
    for letter in plate:
        if letter.isalpha() or letter.isdigit():
            number_of_chars += 1
    return 2 <= number_of_chars <= 6


def is_numbers_at_the_end(plate):
    """
    the first number may not be 0
    after the first number only numbers allowed
    """
    if first_number_index(plate) is None:
        return True
    plate = plate[first_number_index(plate)-1:len(plate)]
    return plate.isdigit() and plate[0] != '0'


def first_number_index(word):
    """
    returns the index of the first number
    """
    index = 0
    for letter in word:
        index += 1
        if letter.isdigit():
            return index
    return None


def is_only_chars_numbers(plate):
    """
    only alphanumberic chars allowed
    """
    for letter in plate:
        if not (letter.isalpha() or letter.isdigit()):
            return False
    return True


if __name__ == "__main__":
    main()
