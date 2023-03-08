"""
CS50. Problem Set 4.

In a file called bitcoin.py, implement a program that:

Expects the user to specify as a command-line argument the number
of Bitcoins, n, that they would like to buy. If that argument
cannot be converted to a float, the program should exit via
sys.exit with an error message. Queries the API for the CoinDesk
Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json,
which returns a JSON object, among whose nested keys is the
current price of Bitcoin as a float. Be sure to catch any exceptions,
as with code like:

import requests

try:
    ...
except requests.RequestException:
    ...
Outputs the current cost of n Bitcoins in USD to four decimal places, using ,
as a thousands separator.

"""

import sys
import json
import requests


def main():
    """
    main function
    """
    check_system_parameter()
    bitcoin_rate = get_bitcoin_rate()
    print_bitcoins(bitcoin_rate)


def get_bitcoin_rate():
    """
    return bitcoin rate as a string
    """
    try:
        api_link = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        req = requests.get(api_link, timeout=5)
        req_json = req.json()
        bitcoin_rate = json.dumps(req_json["bpi"]["USD"]["rate"])
        bitcoin_rate = bitcoin_rate.replace(",", "").replace('"', "")
    except requests.RequestException:
        sys.exit("RequestException")
    return bitcoin_rate


def print_bitcoins(bitcoin_rate):
    """
    prints out the price of the bitcoins
    """
    try:
        bitcoins = float(bitcoin_rate)*float(sys.argv[1])
        print(f"${bitcoins:,.4f}", end="")
    except ValueError:
        sys.exit("Wrong")


def check_system_parameter():
    """
    checks system parameters
    """
    if len(sys.argv) != 2:
        sys.exit("No argument were given")
    try:
        float(sys.argv[1])
    except ValueError:
        sys.exit("Given argument not a float")


if __name__ == "__main__":
    main()
