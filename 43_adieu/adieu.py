"""
CS50. Problem Set 4 Adieu, Adieu.

In a file called adieu.py, implement a program that prompts the user for names
, one per line, until the user inputs control-d.
Assume that the user will input at least one name.
Then bid adieu to those names, separating two names with one and,
three names with two commas and one and, and
names with commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
"""

import inflect

def main():
    name_list = get_names()
    p = inflect.engine()
    print("Adieu, adieu, to",p.join(name_list))


def get_names():
    name_list = []
    while True:
        try:
            name = input("")
            name_list.append(name)
        except EOFError:
            break
    return name_list

if __name__ == "__main__":
    main()