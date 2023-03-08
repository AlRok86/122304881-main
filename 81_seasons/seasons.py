"""
CS50. Problem Set 6. Seasons of Love

In a file called seasons.py, implement a program that
prompts the user for their date of birth in YYYY-MM-DD
format and then sings prints how old they are in minutes
, rounded to the nearest integer, using English words
instead of numerals, just like the song from Rent,
without any and between words. Since a user might not
know the time at which they were born, assume, for
simplicity, that the user was born at midnight (i.e.,
00:00:00) on that date. And assume that the current
time is also midnight. In other words, even if the user
runs the program at noon, assume that it’s actually
midnight, on the same date. Use datetime.date.today
to get today’s date, per
docs.python.org/3/library/datetime.html#datetime.date.today.
"""


from datetime import date
import sys
import inflect


def main():
    """
    prints out minutes since birth in words
    """
    try:
        birthday = get_birthday(input("Date of birth: "))
    except ValueError:
        sys.exit("Wrong Format")
    minutes_since_birth = get_date_diff_in_minutes(date.today(), birthday)
    inflect_engine = inflect.engine()
    print(inflect_engine.number_to_words(minutes_since_birth, andword="")
          .capitalize(),
          "minutes")


def get_birthday(string):
    """
    tries to parse the input into a date, else ValueError
    """
    b_year, b_month, b_day = string.split("-")
    return date(int(b_year), int(b_month), int(b_day))


def get_date_diff_in_minutes(date1, date2):
    """
    returns the difference in minutes, rounded to nearest int
    """
    delta = date1 - date2
    return int(delta.total_seconds() / 60)


if __name__ == "__main__":
    main()
