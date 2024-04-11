#!/usr/bash/python3
def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError ("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an interger")
    x = int(a)
    y = int(b)

    result = x + y
    return result

if __name__ == "__name__":
    import doctest
    doctest.testmod()
