#!/usr/bin/python3
"""
creates an object from json
"""

import json


def load_from_json_file(filename):
    """
    takes filname s a paraeter
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return(data)
