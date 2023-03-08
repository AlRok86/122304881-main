"""
CS50. Problem Set 6. NUMB3RS

In a file called numb3rs.py, implement a function called
validate that expects an IPv4 address as input as a str
and then returns True or False, respectively, if that
input is a valid IPv4 address or not.

"""
import re
import sys


def main():
    """
    prints whether the adress valid or not
    """
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """
    checks if the adress is valid
    """
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        return number_in_range(matches.group(1)) and \
            number_in_range(matches.group(2)) and \
            number_in_range(matches.group(3)) and \
            number_in_range(matches.group(4))
    return False


def number_in_range(string):
    """
    checks if the number is between 0 and 255
    """
    return 0 <= int(string) <= 255


if __name__ == "__main__":
    main()
