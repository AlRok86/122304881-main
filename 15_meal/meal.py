"""
CS50. Problem Set 1. Meal Time.

In meal.py, implement a program that prompts the user for a time
and outputs whether it’s breakfast time, lunch time, or dinner time.
If it’s not time for a meal, don’t output anything at all. Assume that the
user’s input will be formatted in 24-hour time as #:## or ##:##.
And assume that each meal’s time range is inclusive.
For instance, whether it’s 7:00, 7:01, 7:59, or 8:00,
or anytime in between, it’s time for breakfast.
"""


def main():
    user_time = input("What time is it?")
    time = convert(user_time)
    if 6 <= time <= 9:
        print("breakfast time")
    elif 12 <= time <= 14:
        print("lunch time")
    elif 18 <= time <= 20:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    return int(hour) + int(minute)/60.0


if __name__ == "__main__":
    main()
