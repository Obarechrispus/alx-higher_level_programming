#!/usr/bin/python3
def magic_calculation(a, b):
    # Import the 'add' and 'sub' functions from the 'magic_calculation_102' module
    add, sub = __import__('magic_calculation_102', fromlist=('add', 'sub')).add, __import__('magic_calculation_102', fromlist=('add', 'sub')).sub
    
    # Check if 'a' is less than 'b'
    if a < b:
        # If 'a' is less than 'b', calculate 'c' by adding 'a' and 'b'
        c = add(a, b)
        
        # Loop from 4 to 5 (inclusive)
        for i in range(4, 6):
            # Add the current value of 'i' to 'c'
            c = add(c, i)
        
        # Return the final calculated value of 'c'
        return c
    else:
        # If 'a' is not less than 'b', subtract 'b' from 'a' and return the result
        return sub(a, b)
