"""
CS50. Problem Set 1. Math Interpreter.
In a file called interpreter.py, implement a program that prompts
the user for an arithmetic expression and then calculates
and outputs the result as a floating-point value formatted to one
decimal place.
Assume that the user’s input will be formatted as x y z,
with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer
"""


def main():
    """
    calculates a simple math task
    """
    user_input = input("Arithmetic expression: ")
    x, y, z = parse_input(user_input)
    output = calculate_ouput(int(x), y, int(z))
    print(f"{output:.1f}")


def parse_input(user_input):
    """
    parses input by user
    """
    x, y, z = tuple(user_input.lower().strip().split(" "))
    return x, y, z


def calculate_ouput(x, y, z):
    """
    calculates, intepreting the operation
    """
    match y:
        case "+":
            return x + z
        case "-":
            return x - z
        case "*":
            return x * z
        case "/":
            return x / z


main()
