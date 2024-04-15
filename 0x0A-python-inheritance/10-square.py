#!/usr/bin/python3
"""Module defining a Rectangle and Square classes"""


class Rectangle:
    """Class representing a rectangle"""
    def __init__(self, width, height):
        """Initialize rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle"""
        return self.width * self.height


class Square(Rectangle):
    """Class representing a square, inheriting from Rectangle"""
    def __init__(self, size):
        """Initialize square with size"""
        self.__size = 0
        super().__init__(size, size)

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.integer_validator("size", value)
        self.__size = value

    def area(self):
        """Calculate the area of the square"""
        return self.__size ** 2

    def integer_validator(self, name, value):
        """Validate integer values"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

