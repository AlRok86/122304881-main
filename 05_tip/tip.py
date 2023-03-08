"""
CS50. Problem Set 0. Tip Calculator.

In the United States, it’s customary to leave a tip
for your server after dining in a restaurant,
typically an amount equal to 15% or more of your meal’s cost.
"""


def main():
    """
    calculates and prints out the tip
    """
    promt = "How much was the meal? "
    dollars = dollars_to_float(input(promt))
    promt = "What percentage would you like to tip? "
    percent = percent_to_float(input(promt))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollar):
    """
    removes $
    """
    return float(dollar.replace("$", ""))


def percent_to_float(percent):
    """
    transforms percent to float
    """
    return float(percent.replace("%", ""))/100.0


main()
