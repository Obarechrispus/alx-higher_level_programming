#!/usr/bin/python3
"""
Script: append_text_to_file.py

This script imports and utilizes the `append_write` function from another module to append text to a file.

"""
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)
