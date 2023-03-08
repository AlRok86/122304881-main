"""
CS50. Problem Set 2. Coke Machine.

In a file called coke.py, implement a program that prompts
the user to insert a coin, one at a time, each time informing
the user of the amount due. Once the user has inputted at least 50 cents,
output how many cents in change the user is owed. Assume that the user
will only input integers, and ignore any integer
that isn’t an accepted denomination.
"""


def main():
    """
    wants coins till amount is reached
    """
    due_amount = 50
    while due_amount > 0:
        print("Amount due: ", due_amount)
        coin = int(input("Insert coin: "))
        if is_acceptable_coin(coin):
            due_amount -= coin
    print("Change Owed: ", -1 * due_amount)


def is_acceptable_coin(coin):
    """
    is the coin valid?
    """
    return coin in (5, 10, 25)


if __name__ == "__main__":
    main()
