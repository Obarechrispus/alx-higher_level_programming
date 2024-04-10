#!/usr/bin/python3

"""
the doc string to the  Recatngle module
"""


class Rectangle:
    def width(self):
        """
        this function defines a private instance of width which is achieved by .__
        """
        return self.__width
    def width(self, value):
        """
        a fuctionin defining that takes a parameter of value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an interger")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width -= value
    def height(self):
        """
        defines a private instance and retrives it by using .__
        """
        return self.__height
    def height(self, value):
        """
        define s a function height that takes two parameter self and value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
    def __init__(self, width=0, height=0):
        """
      we are initialising the rectangle with self, width and heigh parameters
        """
        self.width = width
        self.height = height


