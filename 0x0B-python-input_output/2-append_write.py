#!/usr/bin/python3
"""
a funtion that appends to the end of a file
"""


def append_write(filename="", text=""):
    """
    takes two parameter filename and text
    uses the utf-8 to convert text to binary
    uses tell to move the cursor to the end and start of the file
    we call file write to to write in the code
    """
    with open(filename, 'a', encoding='utf-8') as a file:
        start = file.tell()
        file.write(text)
        end = file.tell()
        text = end - satrt

        return (text)
