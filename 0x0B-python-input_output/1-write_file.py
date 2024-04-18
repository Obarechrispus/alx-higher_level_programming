#!/usr/bin/python3
"""
A function that takes two parameters filename and text
filename and teext are defined without actual value
and when we call the calue they will adopt new values else considered empty
"""


def write_file(filename="", text=""):
    """
    we W+ to writte into a file
    we use the UTF- to string we are geting is properly converted into binary
    the command file.write calls the recently opened file for writting
    """
    with open(filename, 'w+', encoding='utf-8') as file:
        file.write(text)
        return len(text)
