"""
CS50. Problem Set 3. Grocery list.

In a file called grocery.py, implement a program that prompts
the user for items, one per line, until the user inputs control-d
(which is a common way of ending one’s input to a program).
Then output the user’s grocery list in all uppercase, sorted
alphabetically by item, prefixing each line with the number
of times the user inputted that item.
No need to pluralize the items. Treat the user’s input
case-insensitively.
"""


def main():
    """
    grocery
    """
    get_grocery_list()


def get_grocery_list():
    """
    counts the items in the grocery list
    """
    grocery_list = {}
    while True:
        try:
            grocery_item = input().upper()
            if grocery_item in grocery_list:
                grocery_list[grocery_item] += 1
            else:
                grocery_list[grocery_item] = 1
        except EOFError:
            print()
            break
    for item in sorted(grocery_list.keys()):
        print(grocery_list[item], item)


if __name__ == "__main__":
    main()
