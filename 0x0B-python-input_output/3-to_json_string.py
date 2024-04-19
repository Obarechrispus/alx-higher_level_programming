#!/usr/bin/python3
"""
a function that return the json value of an object
"""


import json


def to_json_string(my_obj):
    """
    takes only one parameter
    we had to import from json
    """
    return json.dumps(my_obj)
