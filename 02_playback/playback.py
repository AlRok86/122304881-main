"""
CS50. Problem Set 0. Playback.

In a file called playback.py, implement a program in Python
that prompts the user for input and then outputs that same input,
replacing each space with ... (i.e., three periods).
"""
# Getting user input
userText = input()

# Replacing spaces by three periods
print(userText.replace(" ", "..."))
