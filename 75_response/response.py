"""
CS50. Problem Set 6. Response Validation

In a file called response.py, using either
validator-collection or validators from PyPI,
implement a program that prompts the user for
an email address via input and then prints Valid
or Invalid, respectively, if the input is a
syntatically valid email address. You may not use
re. And do not validate whether the email address’s
domain name actually exists.

"""
from validator_collection import validators, errors


def main():
    """
    prints if the email is valid
    """
    if validate(input("email: ")):
        print("Valid")
    else:
        print("Invalid")


def validate(email):
    """
    uses the library validator_collection to check the email
    """
    try:
        email = validators.email(email)
        return True
    except errors.InvalidEmailError:
        return False


if __name__ == main():
    main()
