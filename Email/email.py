#! python3
# email.py - Finds email addresses on the clipboard and copies them to the clipboard
# Usage: Copy some text call the program
# Example: >>> email.py

import pyperclip
import re


regexp = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # username
    @ # @ symbol
    (\w)+ # domain name
    (\.[a-zA-Z]{2,4}) # dot-something
    )''', re.VERBOSE)


def main():
    # Find matches in clipboard text.
    text = str(pyperclip.paste())
    matches = []
    for groups in regexp.findall(text):
        emails = groups[0]
        matches.append(emails)

    if len(matches) > 0:
        pyperclip.copy(' -+- '.join(matches))
        print("Email address(es) found:")
        print('\n'.join(matches))
    else:
        print('No email address found.')


if __name__ == "__main__":
    main()
