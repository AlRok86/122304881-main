"""
CS50. Problem Set 3. Fuel Gauge.

In a file called fuel.py, implement a program
that prompts the user for a fraction,
formatted as X/Y, wherein each of X and Y is
an integer, and then outputs, as a
percentage rounded to the nearest integer, how
much fuel is in the tank. If, though,
1% or less remains, output E instead to indicate
that the tank is essentially empty.
And if 99% or more remains, output F instead to
indicate that the tank is essentially full.
If, though, X or Y is not an integer, X is greater
than Y, or Y is 0, instead prompt the
user again. (It is not necessary for Y to be 4.)
Be sure to catch any exceptions like ValueError
or ZeroDivisionError.
"""


def main():
    """
    print the fuel display
    """
    fuel = get_fraction("Fraction: ")
    if fuel <= 0.01:
        print("E")
    elif fuel >= 0.99:
        print("F")
    else:
        print(f"{fuel*100:2.0f}%")


def get_fraction(promt):
    """
    extract fraction as decimal
    """
    while True:
        try:
            user_input = input(promt)
            count, _, denom = user_input.partition("/")
            if int(count)/int(denom) > 1:
                raise ValueError
            return int(count)/int(denom)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


if __name__ == "__main__":
    main()
