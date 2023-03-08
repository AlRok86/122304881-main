"""
CS50. Problem Set 6. Working 9 to 5

In a file called working.py, implement a function
called convert that expects a str in either of the
12-hour formats below and returns the corresponding
str in 24-hour format (i.e., 9:00 to 17:00). Expect
that AM and PM will be capitalized (with no periods
therein) and that there will be a space before each.
Assume that these times are representative of actual
times, not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
Raise a ValueError instead if the input to convert is
not in either of those formats or if either time is
invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not
assume that someone’s hours will start ante meridiem
and end post meridiem; someone might work late and
even long hours (e.g., 5:00 PM to 9:00 AM).

"""
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    re_string_time = r"([0-9][0-9]?)(:[0-9][0-9])? ([AP][M])"
    if matches := re.search(re_string_time + " to " + re_string_time, s):
        start_hour = matches.group(1)
        start_minute = improve_minute(matches.group(2))
        start_meridiem = matches.group(3)
        start_hour = change_hour(start_hour, start_meridiem)
        end_hour = matches.group(4)
        end_minute = improve_minute(matches.group(5))
        end_meridiem = matches.group(6)
        end_hour = change_hour(end_hour, end_meridiem)
        return f"{start_hour}{start_minute} to {end_hour}{end_minute}"
    raise ValueError


def improve_minute(minute):
    if minute is None:
        minute = ":00"
    if 0 <= int(minute[1:]) < 60:
        return minute
    else:
        raise ValueError


def change_hour(hour, meridiem):
    if meridiem == "PM" and hour != "12":
        hour = str(int(hour) + 12)
    if hour == "12" and meridiem == "AM":
        hour = "00"
    if len(hour) == 1:
        hour = "0" + hour
    if 0 <= int(hour) <= 23:
        return hour
    else:
        raise ValueError


if __name__ == "__main__":
    main()
