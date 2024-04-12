#!/usr/bin/python3
"""
A python file that takes two parameter of string, first name and last name. 
"""
def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last name must be a string")
    name = "My name is {} {}".format(first_name, last_name)

    return name


