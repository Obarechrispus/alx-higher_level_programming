#!/usr/bin/python3
"""
a function that return the python data structure as represented by json string
"""

import json


def from_json_string(my_str):
    """
    takes a single parameter
    we use loads instead of dumps
    because we are converting a json into a python
    """
    return json.loads(my_str)
