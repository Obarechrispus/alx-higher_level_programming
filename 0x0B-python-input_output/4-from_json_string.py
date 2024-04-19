#!/usr/bin/python3
"""
a function that return the python data structure as represented by json string
"""

import json


def from_json_string(my_str):
    """
    takes a single parameter
    """
    return json.dumps(my_str)
