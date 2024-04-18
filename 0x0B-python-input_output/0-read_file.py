#!/usr/bin/python3
"""
 It reads the file line by line and prints each line to stdout.
"""


def read_file(filename=""):
    """This function, read_file, takes an optional par
    ameter filename which defaults to an empty string."""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
