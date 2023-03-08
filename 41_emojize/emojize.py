"""
CS50. Problem Set 4. emojize.

In a file called emojize.py, implement a program that
prompts the user for a str in English and then
outputs the “emojized” version of that str, converting
any codes (or aliases) therein to their corresponding emoji.
"""
import emoji

def main():
    text = input().strip()
    print(emoji.emojize(text, language='alias'))

if __name__ == "__main__":
    main()