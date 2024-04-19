#!/usr/bin/python3
"""
A function that writes into a file using the json interpretation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    the objest contains the json scripts while
    the name of the file is filename
    """
    json_str = json.dumps(my_obj)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json_str)
