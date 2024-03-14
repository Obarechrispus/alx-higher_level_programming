#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1  # Subtracting 1 to exclude the script name itself
    if num_args == 0:
        print("{} arguments".format(num_args))
    if num_args == 1:
        print("{} argument:".format(num_args))
    if num_args > 1:
        print("{} arguments:".format(num_args))
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
