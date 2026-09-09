"""
Assignment 5
Problem Statement: PAN Number Validation Using Regular Expression

Write a Python program that accepts a PAN number from the user and validates it
using a regular expression. The program must ensure that the input contains only
the permitted characters - uppercase letters (A-Z) and digits (0-9) - and follows
the standard 10-character PAN format:

    AAAAA9999A

where the first five characters are uppercase letters, the next four are digits,
and the last character is an uppercase letter.

Display "Valid PAN Number" if the input matches the required pattern; otherwise,
display "Invalid PAN Number".

Examples:
ABCDE1234F -> Valid PAN Number
ABCD@1234F -> Invalid PAN Number
ABCDE12345 -> Invalid PAN Number
"""

import re

# Regex pattern: 5 uppercase letters, 4 digits, 1 uppercase letter
PAN_PATTERN = r"^[A-Z]{5}[0-9]{4}[A-Z]$"


def is_valid_pan(pan_number):
    """Return True if pan_number matches the standard PAN format, else False."""
    return bool(re.match(PAN_PATTERN, pan_number))


def main():
    pan_number = input("Enter the PAN number: ").strip()

    if is_valid_pan(pan_number):
        print("Valid PAN Number")
    else:
        print("Invalid PAN Number")


if __name__ == "__main__":
    main()
