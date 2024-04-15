#!/usr/bin/python3
"""
A python file thatinherits from a list
"""

class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the list in sorted order (ascending).
        """
        print(sorted(self))

