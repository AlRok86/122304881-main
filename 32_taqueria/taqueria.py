"""
CS50. Problem Set 3. Fuel taqueria.

In a file called taqueria.py, implement a program that enables a user to
place an order, prompting them for items, one per line, until the user
inputs control-d (which is a common way of ending one’s input to a program).
After each inputted item, display the total cost of all items inputted thus
far, prefixed with a dollar sign ($) and formatted to two decimal places.
Treat the user’s input case insensitively. Ignore any input that isn’t an item.
Assume that every item on the menu will be titlecased.
"""
prices = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }


def main():
    """
    takes the order
    """
    take_order()


def take_order():
    """
    takes the order and counts the price
    """
    total = 0
    while True:
        try:
            meal = input("Which meal? ").title()
            if meal in prices:
                total += tell_price(meal)
            else:
                continue
        except EOFError:
            break
        else:
            print(f"Total: ${total:.2f}")


def tell_price(meal):
    """
    returns the price
    """
    return prices[meal]


if __name__ == "__main__":
    main()
