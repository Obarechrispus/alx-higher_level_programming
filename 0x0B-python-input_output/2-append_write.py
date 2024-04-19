#!/usr/bin/python3
"""
a module thaat appends to the end of the file
"""


def append_write(filename="", text=""):
    """
    takes two parameter filename and text,
    """

    with open(filename, 'a', encoding='utf-8') as a file:
        start = file.tell()
        file.write(text)
        end = file.tell()
        text = end - satrt

        return (text)
