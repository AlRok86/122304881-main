"""
CS50. Problem Set 3. Outdated.

In a file called outdated.py, implement a program that prompts
the user for a date, anno Domini, in month-day-year order,
formatted like 9/8/1636 or September 8, 1636, wherein the
month  in the latter might be any of the values in the list below:
"""


def main():
    """
    date to yy-mm-dd format
    """
    input_date()


def input_date():
    """
    takes the input and gives it to check_date and prints it
    """
    while True:
        try:
            print(check_date(input("Date: ").strip()))
            break
        except ValueError:
            continue
        except UnboundLocalError:
            continue
        except EOFError:
            break


def check_date(date):
    """
    extracts year, month, day and puts into a proper format
    """
    if date.find("/") > 0:
        month, day, year = date.split("/")
    elif date.find(",") > 0:
        possible_months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]
        month, day, year = date.split(" ")
        day = day[0:-1]
        month = str(possible_months.index(month) + 1)
    if int(month) > 12 or int(month) < 1 or int(day) < 1 or int(day) > 31:
        raise ValueError
    if len(str(month)) == 1:
        month = "0" + str(month)
    if len(day) == 1:
        day = "0" + day
    return year + "-" + month + "-" + day


if __name__ == "__main__":
    main()
