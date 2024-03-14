#!/usr/bin/python3
import sys

def main():
    argument = sys.argv[1:]
    total = 0
    for arg in argument:
        total += int(arg)
    print(total)

if __name__ == "__main__":
    main()
