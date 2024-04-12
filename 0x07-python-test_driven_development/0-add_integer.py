#!/usr/bin/python3
"""
my python file to be used with a testsfile
"""


def add_integer(a, b=98):
    """
    a funtion that add two numbers and the function is called add_integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an interger")
    x = int(a)
    y = int(b)

    result = x + y
    return result
