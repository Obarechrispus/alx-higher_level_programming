#!/usr/bin/python3


def append_write(filename="", text=""):

    with open(filename, 'a', encoding='utf-8') as a file:
        start = file.tell()
        file.write(text)
        end = file.tell()
        text = end - satrt

        return (text)
