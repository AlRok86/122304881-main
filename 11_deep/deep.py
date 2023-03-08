"""
CS50. Problem Set 1. Deep Thought.

In deep.py, implement a program that prompts the user
for the answer to the Great Question of Life, the Universe and Everything,
outputting Yes if the user inputs 42 or (case-insensitively)
forty-two or forty two. Otherwise output No.
"""


def main():
    """
    lets the user answer the great question
    """
    promt = "What is your answer to the " + \
        "Great Question of Life, the Universe and Everything?"
    user_answer = input(promt)
    if is_correct_answer(user_answer):
        print("Yes")
    else:
        print("No")


def is_correct_answer(answer):
    """
    checks the answer to the great question
    """
    return answer.strip() == "42" or \
        answer.lower().strip().replace("-", " ") == "forty two"


main()
