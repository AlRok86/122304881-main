"""
CS50. Problem Set 6. Regular, um, Expressions

In a file called um.py, implement a function called
count that expects a line of text as input as a str
and returns, as an int, the number of times that “um”
appears in that text, case-insensitively, as a word
unto itself, not as a substring of some other word.
For instance, given text like hello, um, world, the
function should return 1. Given text like yummy,
though, the function should return 0.

"""

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    res1 = re.findall(r"[\W]um[\W]", s, re.IGNORECASE)
    res2 = re.findall(r"^um[\W]", s, re.IGNORECASE)
    res3 = re.findall(r"[\W]um$", s, re.IGNORECASE)
    res4 = re.findall(r"^um$", s, re.IGNORECASE)
    print(res1, res2, res3, res4)
    """
    s = " " + s + " "
    re_string = r"^.*[\W\s]*um([\W].*)$"
    while True:
        if matches := re.search(re_string, s, re.IGNORECASE):
            s =  matches.group(1)
            print("middle", s)
            count += 1
        else:
            break
    """
    return len(res1) + len(res2) + len(res3) + len(res4)



if __name__ == "__main__":
    main()
